# 🎥 AI 影片剪輯測試與示範專案：新竹之美 (The Beauty of Hsinchu)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Resolution: 1080p](https://img.shields.io/badge/Resolution-1080p_16%3A9-blue.svg)]()
[![FPS: 30](https://img.shields.io/badge/FPS-30_Zero_Frame_Drop-green.svg)]()

本專案為 **AI Agent 影音剪輯與自動化生成能力** 的實驗與測試範例。展示 AI 如何從網路搜尋開放授權圖片、自動處理音訊與視覺動態、設計中文美學字型與玻璃擬態字幕卡，並最終渲染出完全零掉幀的高畫質 1080p MP4 影片。

👉 🍿 **[▶ 點此線上觀看 60 秒高畫質影片 (hsinchu_beauty.mp4)](https://n0b0dy-is-me.github.io/ai-gen-video-demo/hsinchu_beauty.mp4)**

---

## 🎯 適用場景 (Applicable Scenarios & Use Cases)

本專案所展現的 AI 自動化影音剪輯流程，特別適用於以下場景：

1. **學校課程與教學簡報（非以訓練剪輯技術為目的）**：
   * 適用於地理、歷史、社會、人文藝術、通識課程或語言學習等作業與簡報。
   * **效益**：當課程目標是「主題內容表達、景點人文介紹或視覺導覽」，而非要求學生學習剪輯軟體操作技術時，可大幅降低影音製作門檻，讓學生專注於內容研究與報告品質本身。

2. **輕量級商業與行銷推廣需求**：
   * 適用於社群小編、小微企業、自媒體創作者、房產建案展示、旅遊推廣或產品圖片展示。
   * **效益**：無需耗費高額預算聘請剪輯團隊或購買專業軟體，即可快速生成動態流暢且具備背景音樂與字幕的高質感 1080p 形象短片。

---

## 🌟 亮點與技術特色 (Highlights & Technical Highlights)

1. **完全零掉幀 (Zero Frame Drop Guarantee)**：
   * 採用 Python (Pillow/FFmpeg Pipe) 進行 **逐幀渲染 (Frame-by-Frame Rendering)**，完全不受電腦即時硬體效能影響，100% 輸出穩定 30 FPS 的 1080p H.264 影片。
2. **Ken Burns 鏡頭動態 (Dynamic Motion)**：
   * 為每張靜態照片動態計算縮放（Zoom）與平移（Pan），讓風景照呈現如紀錄片般流暢的動態視野。
3. **中文美學與玻璃擬態 (Glassmorphism & Typography)**：
   * 自動整合 Noto Serif / Sans CJK 字型，搭配淡黑半透明玻璃擬態字幕卡與金色視覺線條。
4. **線上隨點即看 (Online Video Playback)**：
   * 影片託管於 GitHub Pages，無需下載龐大檔案即可在瀏覽器直接順暢觀看。

---

## 🚀 如何請 AI 幫您自動剪輯影片？(新手萌新零基礎指南)

不懂寫程式？不會用複雜的剪輯軟體？別擔心！本影片完全是由 **Google Antigravity** AI 助手全自動剪輯完成的。您只需要直接給 AI 本專案的 GitHub 網址，就能讓 AI 自動為您量身打造一部精美影片！

### 步驟 1：下載安裝 Antigravity 軟體
1. 點擊前往 🌐 **[Google Antigravity 官方下載頁面](https://antigravity.google/download)**。
2. 畫面中會有多個版本選項，**請直接選擇並下載「Antigravity 2.0」** 桌面應用程式（適用於您的 Windows 或 Mac 電腦）。

### 步驟 2：開啟對話視窗
1. 安裝完成後開啟 **Antigravity 2.0** 軟體。
2. 您會看到一個非常親切的 AI 聊天對話視窗。

### 步驟 3：直接傳送指令給 AI！
複製下方這句話，貼到 Antigravity 聊天視窗傳送給 AI 即可：

> 💬 **「我想做出跟 https://github.com/n0b0dy-is-me/ai-gen-video-demo/ 類似的影片，請僅下載 main 分支的內容來查看，並依照 TEMPLATE.md 和我詳細討論影片的規劃。」**

### 步驟 4：坐等影片完成！
* AI 助手讀取連結與需求後，會先依照 `TEMPLATE.md` 和您討論確認主題、風格與細節，確認後會自動在背景幫您：
  * 搜尋高解析度美麗照片
  * 搭配優雅的背景音樂
  * 加上漂亮的中文標題與字幕
  * 自動剪輯並輸出成高畫質影片檔案
* 您完全不需要安裝複雜的剪輯工具，也不需要輸入任何艱深的電腦指令，一切交給 AI 全自動處理即可！

---

## 📁 專案目錄結構 (Repository Structure)

```text
beauty_of_hsinchu/ (main 分支 - 輕量化無大型影片檔)
├── README.md               # 專案介紹、適用場景與新手操作說明
├── TEMPLATE.md             # 使用者要求 AI 剪輯類似影片的需求模板
├── SOURCES.md              # 圖片與音樂版權/出處標示
├── CHAT_HISTORY.md         # 使用者與 AI 互動的完整對話歷程紀錄
├── LICENSE                 # MIT 開源授權條款
├── assets/                 # 高解析度素材與背景音樂 (bgm.mp3)
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

> 💡 **影片媒體檔線上觀看**：高畫質影片檔已託管於 GitHub Pages 頁面，點此立即線上播放：[https://n0b0dy-is-me.github.io/ai-gen-video-demo/hsinchu_beauty.mp4](https://n0b0dy-is-me.github.io/ai-gen-video-demo/hsinchu_beauty.mp4)。

---

## 💬 對話歷史紀錄 (Chat History)

您可以在 [CHAT_HISTORY.md](CHAT_HISTORY.md) 查閱使用者與 AI 助手從最初的需求討論、方案評估、素材下載到影片生成與專案整理的全過程對話紀錄。

---

## 📝 授權與創用 CC 說明 (License & Attribution)

* 本專案程式碼與模板採 [MIT License](LICENSE) 開源授權。
* 照片與音樂素材採用 Wikimedia Commons / Unsplash 開放授權，詳細來源與作者列表請參閱 [SOURCES.md](SOURCES.md)。
