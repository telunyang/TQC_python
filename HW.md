# 作業須知

## 作業
- 僅限授課學員。
- 同學之間可以互相討論，但千萬不要抄襲。
- 自行設計 `compare.bat` 的替代品，名稱自取；**可以搭配 AI 來開發**。
  - 使用 `.py` 或是 `ipynb`，或是網頁相關的應用程式（如果有學過，例如 `flask` 或 `django`），來開發一個可以用來比較兩個`.py`執行結果的程式（可參考 [compare.bat](./compare.bat)），風格自訂。
  - `80` 分條件
    - `錄製`執行過程，並提供`影片連結`，可以放在 `YouTube` 或是 `Google Drive`。
    - 不用給我看程式碼，錄製的時候直接展示比較兩個程式執行的結果。
    - 至少要比較 **3** 個題目（題目自選），其中一題必須是第 **9** 類需要讀取或寫入檔案的題目。
      - 如果是寫入檔案的題目，需要比較寫入檔案的內容。
      - 每一個題目都要展示**判斷為正確**的結果和**判斷為錯誤**的結果。
  - `95` 分條件 (基於 `80` 分條件)
    - 使用 `GitHub` 平台來提交作業，並且將 `github repo 連結` 以及 `影片連結` 連結寄給我。
      - Git 與 GitHub 使用教學: [程式與網頁開發者必備技能！Git 和 GitHub 零基礎快速上手，輕鬆掌握版本控制的要訣！](https://www.youtube.com/watch?v=FKXRiAiQFiY)
      - Markdown 語法: [如何使用 Markdown 語言撰寫技術文件](https://experienceleague.adobe.com/zh-hant/docs/contributor/contributor-guide/writing-essentials/markdown)
    - `repository` 裡面要有你的原始碼和相關檔案，以及 `README.md`。
      ```
      app.py
      ...
      README.md
      ```
    - `README.md` 要說明執行指令或方法，例如:
      ```markdown
      # 你自製的 code judger 名稱
      這裡可以簡單說明一下你自製的 code judger 的簡介、功能和使用方法。

      ## 套件列表
      - flask (版本號)
      - .... (版本號)
      ...
      (版本號可用 pip list，或是 conda list 來檢視)
      ...

      ## 成果
      ![](執行過程的擷圖或說明圖片)
      ...
      [影片名稱或其它標題](你的影片連結)
      ...

      ## 其它你想要補充標題和內容
      ...
      ...
      ```
  - `100` 分條件 (基於 `95` 分條件)
    - 一種感覺。
  - 可以參考以前的人所撰寫的 README: [https://github.com/huangcody/nlp_bert](https://github.com/huangcody/nlp_bert)
  - 沒交：`60` 分。
- 繳交時間
  - 原則上最後一堂課結束後 2 週內，準確時間上課說明。