#!/usr/bin/env python3
"""
AI Agent Automated Video Generator Script
------------------------------------------
Renders a 1080p landscape slideshow video from a directory of photos,
with Ken Burns pan/zoom, CJK typography overlays, crossfade transitions,
and AAC background music with volume fading.
"""

import os
import sys
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Configuration
WIDTH, HEIGHT = 1920, 1080
FPS = 30
DURATION_TOTAL = 60.0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
PHOTOS_DIR = os.path.join(PROJECT_DIR, 'photos')
OUTPUT_VIDEO = os.path.join(PROJECT_DIR, 'hsinchu_beauty.mp4')
BGM_PATH = os.path.join(PHOTOS_DIR, 'bgm.mp3')

# Fonts
FONT_SERIF_BOLD = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
FONT_SANS_REG = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
FONT_SANS_BOLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'

# Default Scenes Data
DEFAULT_SCENES = [
    {
        'image': 'east_gate.jpg',
        'tag': '【 迎曦門 】',
        'title': '迎曦古城 ‧ 歷史風華',
        'subtitle': '築城二百年，新竹璀璨的文化地標與歷史記憶',
        'zoom_start': 1.02, 'zoom_end': 1.12, 'pan': (0, -10)
    },
    {
        'image': 'xiangshan_wetland.jpg',
        'tag': '【 香山濕地 】',
        'title': '香山濕地 ‧ 潮間生態',
        'subtitle': '漫步賞蟹步道，感受大海與夕陽交織的自然樂章',
        'zoom_start': 1.10, 'zoom_end': 1.02, 'pan': (10, 0)
    },
    {
        'image': 'smangus.jpg',
        'tag': '【 司馬庫斯 】',
        'title': '司馬庫斯 ‧ 黑色部落',
        'subtitle': '霧林深處的千年巨木，上帝留給風城最純淨的仙境',
        'zoom_start': 1.03, 'zoom_end': 1.13, 'pan': (-10, -5)
    },
    {
        'image': 'hsinchu_coastline.jpg',
        'tag': '【 17公里海岸線 】',
        'title': '十七公里海岸 ‧ 追風巡禮',
        'subtitle': '騎行於綿延海岸線，擁抱九降風與蔚藍海天',
        'zoom_start': 1.08, 'zoom_end': 1.00, 'pan': (5, 10)
    },
    {
        'image': 'hsinchu_mountain_fog.jpg',
        'tag': '【 尖石群山 】',
        'title': '尖石群山 ‧ 雲霧繚繞',
        'subtitle': '山嵐與壯麗峽谷交錯，走進新竹後花園的靜謐秘境',
        'zoom_start': 1.01, 'zoom_end': 1.10, 'pan': (0, 10)
    },
    {
        'image': 'hsinchu_sunset_sea.jpg',
        'tag': '【 香山落日 】',
        'title': '香山落日 ‧ 晚霞餘暉',
        'subtitle': '金黃餘暉灑落海面，捕捉風城最動人的夕陽時刻',
        'zoom_start': 1.12, 'zoom_end': 1.03, 'pan': (-10, 0)
    },
    {
        'image': 'hsinchu_ancient_temple.jpg',
        'tag': '【 歷史古蹟 】',
        'title': '百年信仰 ‧ 人文風情',
        'subtitle': '香火鼎盛的新竹城隍廟，承載道地美食與世代故事',
        'zoom_start': 1.03, 'zoom_end': 1.12, 'pan': (0, -10)
    },
    {
        'image': 'hsinchu_night_view.jpg',
        'tag': '【 璀璨風城 】',
        'title': '科技與古都 ‧ 璀璨夜色',
        'subtitle': '融合科技脈動與古都底蘊，迎向明亮繁華的夜色',
        'zoom_start': 1.00, 'zoom_end': 1.10, 'pan': (10, -5)
    }
]

def prepare_base_image(path):
    img = Image.open(path).convert('RGB')
    iw, ih = img.size
    target_ratio = WIDTH / HEIGHT
    img_ratio = iw / ih

    if img_ratio > target_ratio:
        new_w = int(ih * target_ratio)
        offset = (iw - new_w) // 2
        img = img.crop((offset, 0, offset + new_w, ih))
    else:
        new_h = int(iw / target_ratio)
        offset = (ih - new_h) // 2
        img = img.crop((0, offset, iw, offset + new_h))
    
    return img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

def main():
    print("Preparing image frames...")
    loaded_images = []
    for sc in DEFAULT_SCENES:
        p = os.path.join(PHOTOS_DIR, sc['image'])
        loaded_images.append(prepare_base_image(p))

    # Fonts
    title_font = ImageFont.truetype(FONT_SERIF_BOLD, 54, index=0)
    tag_font = ImageFont.truetype(FONT_SANS_BOLD, 26, index=0)
    sub_font = ImageFont.truetype(FONT_SANS_REG, 28, index=0)
    cover_title_font = ImageFont.truetype(FONT_SERIF_BOLD, 76, index=0)
    cover_sub_font = ImageFont.truetype(FONT_SANS_REG, 34, index=0)
    counter_font = ImageFont.truetype(FONT_SANS_REG, 24, index=0)

    def render_scene_frame(scene_idx, progress):
        sc = DEFAULT_SCENES[scene_idx]
        base = loaded_images[scene_idx]
        
        zoom = sc['zoom_start'] + (sc['zoom_end'] - sc['zoom_start']) * progress
        pan_x = sc['pan'][0] * progress
        pan_y = sc['pan'][1] * progress
        
        zw = int(WIDTH / zoom)
        zh = int(HEIGHT / zoom)
        zx = max(0, min(WIDTH - zw, (WIDTH - zw) // 2 + int(pan_x)))
        zy = max(0, min(HEIGHT - zh, (HEIGHT - zh) // 2 + int(pan_y)))
        
        frame = base.crop((zx, zy, zx + zw, zy + zh)).resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR)
        draw = ImageDraw.Draw(frame, 'RGBA')
        
        # Bottom gradient overlay
        gradient = Image.new('RGBA', (WIDTH, 340), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(gradient)
        for y in range(340):
            alpha = int(210 * (y / 340.0) ** 1.3)
            g_draw.line([(0, y), (WIDTH, y)], fill=(10, 15, 25, alpha))
        frame.paste(gradient, (0, HEIGHT - 340), gradient)
        
        # Card Box
        box_w, box_h = 1100, 200
        box_x, box_y = 100, HEIGHT - 260
        overlay_card = Image.new('RGBA', (box_w, box_h), (15, 23, 42, 140))
        frame.paste(overlay_card, (box_x, box_y), overlay_card)
        draw.rectangle([box_x, box_y, box_x + 6, box_y + box_h], fill=(234, 179, 8, 240))
        
        draw.text((box_x + 35, box_y + 22), sc['tag'], font=tag_font, fill=(250, 204, 21, 255))
        draw.text((box_x + 35, box_y + 60), sc['title'], font=title_font, fill=(255, 255, 255, 255))
        draw.text((box_x + 35, box_y + 138), sc['subtitle'], font=sub_font, fill=(226, 232, 240, 240))
        
        counter_str = f"【 新竹之美 】  {scene_idx + 1:02d} / {len(DEFAULT_SCENES):02d}"
        draw.text((WIDTH - 240, HEIGHT - 80), counter_str, font=counter_font, fill=(203, 213, 225, 220))
        draw.text((100, 60), "HSINCHU, TAIWAN ‧ 風城景象", font=tag_font, fill=(255, 255, 255, 190))
        draw.line([(100, 100), (380, 100)], fill=(250, 204, 21, 200), width=3)
        return frame

    def render_cover_frame(progress):
        base = loaded_images[0].filter(ImageFilter.GaussianBlur(15))
        frame = ImageEnhance.Brightness(base).enhance(0.4)
        draw = ImageDraw.Draw(frame, 'RGBA')
        margin = 80
        draw.rectangle([margin, margin, WIDTH - margin, HEIGHT - margin], outline=(250, 204, 21, 180), width=2)
        draw.text((WIDTH // 2 - 320, HEIGHT // 2 - 120), "新 竹 之 美", font=cover_title_font, fill=(255, 255, 255, 255))
        draw.text((WIDTH // 2 - 280, HEIGHT // 2 + 10), "風城風華 ‧ 璀璨大地與人文特輯", font=cover_sub_font, fill=(253, 224, 71, 240))
        draw.line([(WIDTH // 2 - 150, HEIGHT // 2 + 75), (WIDTH // 2 + 150, HEIGHT // 2 + 75)], fill=(255, 255, 255, 200), width=2)
        draw.text((WIDTH // 2 - 140, HEIGHT // 2 + 100), "A VISUAL JOURNEY OF HSINCHU", font=tag_font, fill=(203, 213, 225, 200))
        return frame

    def render_outro_frame(progress):
        base = loaded_images[-1].filter(ImageFilter.GaussianBlur(18))
        frame = ImageEnhance.Brightness(base).enhance(0.35)
        draw = ImageDraw.Draw(frame, 'RGBA')
        draw.text((WIDTH // 2 - 300, HEIGHT // 2 - 80), "遇 見 新 竹 ‧ 記 住 美 好", font=cover_title_font, fill=(255, 255, 255, 255))
        draw.text((WIDTH // 2 - 220, HEIGHT // 2 + 30), "願這份熱情與風采，常伴您左右", font=cover_sub_font, fill=(253, 224, 71, 240))
        return frame

    ffmpeg_cmd = [
        'ffmpeg', '-y', '-f', 'rawvideo', '-vcodec', 'rawvideo',
        '-s', f'{WIDTH}x{HEIGHT}', '-pix_fmt', 'rgb24', '-r', str(FPS),
        '-i', '-', '-i', BGM_PATH,
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
        '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
        '-af', f'afade=t=in:ss=0:d=1.5,afade=t=out:st={DURATION_TOTAL-2.5}:d=2.5',
        '-t', str(DURATION_TOTAL), '-shortest', OUTPUT_VIDEO
    ]

    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    total_frames = int(DURATION_TOTAL * FPS)
    COVER_DUR, SCENE_DUR, OUTRO_DUR, FADE_DUR = 3.0, 6.5, 5.0, 1.0

    print(f"Rendering {total_frames} frames to {OUTPUT_VIDEO}...")
    for frame_idx in range(total_frames):
        t = frame_idx / float(FPS)
        if t < COVER_DUR:
            frame_img = render_cover_frame(t / COVER_DUR)
        else:
            t_scenes = t - COVER_DUR
            total_scenes_dur = len(DEFAULT_SCENES) * SCENE_DUR
            if t_scenes < total_scenes_dur:
                sc_idx = min(int(t_scenes // SCENE_DUR), len(DEFAULT_SCENES) - 1)
                sc_t = (t_scenes % SCENE_DUR) / SCENE_DUR
                rem_in_sc = SCENE_DUR - (t_scenes % SCENE_DUR)
                if rem_in_sc < FADE_DUR and sc_idx < len(DEFAULT_SCENES) - 1:
                    curr_f = render_scene_frame(sc_idx, sc_t)
                    next_f = render_scene_frame(sc_idx + 1, 0.0)
                    frame_img = Image.blend(curr_f, next_f, (FADE_DUR - rem_in_sc) / FADE_DUR)
                else:
                    frame_img = render_scene_frame(sc_idx, sc_t)
            else:
                t_outro = t_scenes - total_scenes_dur
                if t_outro < FADE_DUR:
                    last_f = render_scene_frame(len(DEFAULT_SCENES) - 1, 1.0)
                    outro_f = render_outro_frame(t_outro / OUTRO_DUR)
                    frame_img = Image.blend(last_f, outro_f, t_outro / FADE_DUR)
                else:
                    frame_img = render_outro_frame(t_outro / OUTRO_DUR)

        proc.stdin.write(frame_img.tobytes())

    proc.stdin.close()
    proc.wait()
    print("Render finished successfully!")

if __name__ == '__main__':
    main()
