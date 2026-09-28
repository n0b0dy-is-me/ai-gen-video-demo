# 🎥 AI 影片剪輯測試與示範專案：新竹之美 (The Beauty of Hsinchu)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Resolution: 1080p](https://img.shields.io/badge/Resolution-1080p_16%3A9-blue.svg)]()
[![FPS: 30](https://img.shields.io/badge/FPS-30_Zero_Frame_Drop-green.svg)]()

本專案為 **AI Agent 影音剪輯與自動化生成能力** 的實驗與測試範例。展示 AI 如何從網路搜尋開放授權圖片、自動處理音訊與視覺動態、設計中文美學字型與玻璃擬態字幕卡，並最終渲染出完全零掉幀的高畫質 1080p MP4 影片與互動式 HTML5 簡報。

---

## 🎯 適用場景 (Applicable Scenarios & Use Cases)

本專案所展現的 AI 自動化影音剪輯流程，特別適用於以下場景：

1. **學校課程與教學簡報（非以訓練剪輯技術為目的）**：
   * 適用於地理、歷史、社會、人文藝術、通識課程或語言學習等作業與報告。
   * **優勢**：當課程的核心目標是「主題內容表達、景點人文介紹或視覺導覽」，而非要求學生學習 Premiere/Final Cut 等專業剪輯軟體操作時，透過此 AI 工具可大幅降低影音製作門檻，讓學生專注於知識內容本身。

2. **輕量級商業與行銷推廣需求**：
   * 適用於社群小編、小微企業、自媒體創作者、房產展示、旅遊推廣或產品相片展示。
   * **優勢**：無需耗費高額預算聘請剪輯團隊或購買專業軟體，即可快速生成質感極佳、動態流暢且具備背景音樂與字幕的 1080p 形象短片。

---

## 🌟 亮點與測試項目 (Highlights & Benchmarks)

1. **完全零掉幀 (Zero Frame Drop Guarantee)**：
   * 採用 Python (Pillow/FFmpeg Pipe) 進行 **逐幀渲染 (Frame-by-Frame Rendering)**，完全不受電腦即時硬體效能影響，100% 輸出穩定 30 FPS 的 1080p H.264 影片。
2. **Ken Burns 鏡頭動態 (Dynamic Motion)**：
   * 為每張靜態照片動態計算縮放（Zoom）與平移（Pan），讓風景照呈現如紀錄片般流暢的動態視野。
3. **中文美學與玻璃擬態 (Glassmorphism & Typography)**：
   * 自動整合 Noto Serif / Sans CJK 字型，搭配淡黑半透明玻璃擬態字幕卡與金色視覺線條。
4. **雙重交付成果 (Dual Output)**：
   * **MP4 影片檔**：隨處可播放的 1 分鐘高畫質影片。
   * **HTML5 網頁**：可以在任何現代瀏覽器開啟並互動展演的響應式網頁。

---

## 📁 專案目錄結構 (Repository Structure)

```text
beauty_of_hsinchu/
├── README.md               # 專案介紹、適用場景與執行說明
├── TEMPLATE.md             # 使用者要求 AI 剪輯類似影片的需求模板
├── SOURCES.md              # 圖片與音樂版權/出處標示
├── CHAT_HISTORY.md         # 使用者與 AI 互動的完整對話歷程紀錄
├── LICENSE                 # MIT 開源授權條款
├── index.html              # 互動式 HTML5 網頁展演檔
├── hsinchu_beauty.mp4      # 最終生成的 1080p 60秒 MP4 影片
├── photos/                 # 高解析度素材與背景音樂 (bgm.mp3)
│   ├── east_gate.jpg
│   ├── xiangshan_wetland.jpg
│   ├── smangus.jpg
│   ├── hsinchu_coastline.jpg
│   ├── hsinchu_mountain_fog.jpg
│   ├── hsinchu_sunset_sea.jpg
│   ├── hsinchu_ancient_temple.jpg
│   ├── hsinchu_night_view.jpg
│   └── bgm.mp3
├── scripts/                # 自動化渲染指令碼
│   └── render_video.py     # 核心影片渲染 Python 腳本
└── agent_guide/            # 供其他 AI Agent 快速復刻的指令與規範指南
    └── README.md           # AI Agent 操作指南 (Workflow Guide for AI)
```

---

## 💬 對話歷史紀錄 (Chat History)

您可以在 [CHAT_HISTORY.md](CHAT_HISTORY.md) 查閱使用者與 AI 助手從最初的需求討論、方案評估、素材下載到影片生成與專案整理的全過程對話紀錄。

---

## 🚀 如何重新渲染或自訂影片 (How to Run / Reproduce)

### 環境需求 (Prerequisites)
* Python 3.8+
* `ffmpeg` (已安裝並加入系統 PATH)
* Python 套件：`Pillow` (`pip install Pillow`)

### 執行渲染
在 Terminal 中執行以下指令即可重新渲染影片：

```bash
python3 scripts/render_video.py
```

影片將自動輸出至 `hsinchu_beauty.mp4`！

---

## 📝 授權與創用 CC 說明 (License & Attribution)

* 本專案程式碼與模板採 [MIT License](LICENSE) 開源授權。
* 照片與音樂素材採用 Wikimedia Commons / Unsplash 開放授權，詳細來源與作者列表請參閱 [SOURCES.md](SOURCES.md)。
