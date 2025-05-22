# Quantitative-Analysis-Dashboard

這是一個用 Python 實作的技術分析與多因子投資組合優化儀表板，功能包含：

- 自動從 Yahoo Finance 抓取股票歷史價格
- 計算移動平均線、報酬率、年化報酬率、年化波動率、夏普率
- 顯示股價走勢與技術指標圖表
- 顯示夏普率長條圖和報酬率相關係數熱圖
- 使用 Riskfolio-Lib 進行投資組合優化，並繪製組合權重圖

## 環境建置

1. 建議使用 Python 3.8 以上版本
2. 安裝依賴套件：
yfinance
pandas
numpy
matplotlib
seaborn
riskfolio-lib
