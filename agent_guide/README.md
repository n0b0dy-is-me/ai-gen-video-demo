# 🤖 AI Agent 影音剪輯標準作業指南 (AI Agent Execution Playbook)

本指南旨在供任何接續處理影音生成任務的 **AI Agent**（如 Antigravity, Claude, ChatGPT, Cursor 等）快速閱讀，掌握自動化圖片蒐集、影音渲染與頁面生成的完整 SOP。

---

## ⚡ 核心執行流程 (Standard Operating Procedure)

當使用者發出「幫我蒐集某主題圖片並製作影片」的需求時，請依照以下 4 步驟執行：

### 步驟 1：素材蒐集 (Image & Audio Collection)
1. 建立目標素材資料夾：`mkdir -p photos/`
2. 使用 Python urllib 搭配 **Wikimedia Commons API** 或 **Unsplash Direct URLs** 抓取高解析度照片 (建議 6 ~ 10 張)。
3. 使用 Wikimedia Commons 搜尋並下載 CC0 / CC-BY 公眾領域背景音樂（如古典鋼琴、鋼琴輕音樂），儲存為 `photos/bgm.mp3`。

### 步驟 2：執行影片渲染 (Render Video)
1. 確保系統已安裝 `python3`, `ffmpeg`, 及 `Pillow` 套件。
2. 執行指令：
   ```bash
   python3 scripts/render_video.py
   ```
3. 渲染腳本說明：
   * **逐幀 Pipe 寫入 FFmpeg**：避免 Chrome 即時錄影掉幀問題。
   * **Ken Burns 特效**：透過 Pillow 動態計算照片 `crop` 與 `resize` 實現微縮放與平移。
   * **文字與排版**：使用系統內建 `NotoSerifCJK-Bold.ttc` 與 `NotoSansCJK-Regular.ttc` 繪製半透明玻璃擬態字幕卡。
   * **音樂處理**：FFmpeg 自動加入音訊 `afade` 效果（前 1.5 秒淡入，最後 2.5 秒淡出）。

### 步驟 3：同步生成 HTML 簡報頁面 (Generate HTML Showcase)
1. 產生與影片對應的 16:9 響應式 HTML5 頁面 `index.html`。
2. 包含 CSS 轉場 (`transition: opacity 1.2s`) 與 Ken Burns 縮放 (`scale(1.02) -> scale(1.12)`).
3. 提供 `<audio>` 播放器與 MediaRecorder 備用按鈕。

### 步驟 4：出處紀錄 (Attribution & Documentation)
1. 建立 `SOURCES.md` 紀錄所有素材的原始連結與創用 CC 授權條款。
2. 建立 `TEMPLATE.md` 與 `README.md` 交付使用者。

---

## 🛠️ 常見問題與排障 (Troubleshooting)

* **Wikimedia API 429 Rate Limit Error**：
  * 原因：短時間內重複呼叫 `commons.wikimedia.org/w/api.php`。
  * 解決方法：在請求標頭（User-Agent）帶入自訂 App 名稱，並在請求間隔加上 `time.sleep(1.5)`。
* **中文 CJK 字型找不到**：
  * 使用 Linux 標準字型路徑 `/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc` 或 `/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc`。
