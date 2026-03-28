Project Title

Trader Behavior Analysis using Market Sentiment (Fear & Greed Index)

 Project Description

This project analyzes the relationship between Bitcoin market sentiment (Fear/Greed Index) and trader performance using historical trading data from Hyperliquid.

The goal is to uncover patterns in trader profitability, win rates, and behavior under different market sentiment conditions.

 Problem Statement

Understanding how market sentiment influences trading outcomes is critical for designing better trading strategies.

This project aims to:

Analyze trader performance across different sentiment phases
Identify patterns in profitability and success rates
Provide insights for sentiment-aware trading strategies
 Features
Data cleaning and preprocessing of real-world trading data
Timestamp alignment and dataset merging
Profitability analysis (PnL by sentiment)
Win rate analysis
Identification of top-performing traders
Visualization of trading performance trends
 Technologies Used
Python
Pandas
Matplotlib
Seaborn
Jupyter Notebook / VS Code
 Project Workflow
Data Collection
      ↓
Data Cleaning & Preprocessing
      ↓
Feature Engineering (Date Alignment)
      ↓
Dataset Merging
      ↓
Exploratory Data Analysis (EDA)
      ↓
Performance Analysis (PnL, Win Rate)
      ↓
Visualization & Insights
 Folder Structure
Trader_Sentiment_Analysis/
│
├── data/
│   ├── raw/
│   │   ├── historical_data.csv
│   │   └── fear_greed_index.csv
│   └── processed/
│       └── merged_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── analysis.py
│   └── visualization.py
│
├── outputs/
│   └── plots/
│       ├── pnl_boxplot.png
│       └── avg_pnl.png
│
├── notebooks/
│   └── analysis.ipynb
│
├── requirements.txt
└── README.md
 Installation & Setup
1. Clone Repository
git clone <your-repo-link>
cd Trader_Sentiment_Analysis
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Requirements
pip install -r requirements.txt
4. Run the Project
jupyter notebook

Open analysis.ipynb and run all cells.

 Key Results
🔹 PnL Summary by Sentiment
Highest average profit observed during Extreme Greed
Lower profitability during Fear and Extreme Fear
🔹 Win Rate Analysis
Highest win rate during Extreme Greed (~46%)
Lowest win rate during Extreme Fear (~37%)
🔹 Trader Distribution
A small number of traders generate the majority of profits
Indicates a skewed (power-law) distribution of returns
 Key Insights
Market sentiment strongly influences trader performance
Traders perform better in bullish (Greed) conditions
Fear-driven markets lead to lower success rates
Profit distribution is highly uneven — few traders dominate gains
 Conclusion

This analysis demonstrates that incorporating market sentiment into trading strategies can significantly improve decision-making.

Traders may benefit from:

Increasing exposure during Greed phases
Applying stricter risk management during Fear phases
 Future Improvements
Add advanced metrics (Sharpe Ratio, Drawdown)
Build an interactive dashboard (Streamlit)
Perform trader segmentation (beginner vs expert)
Apply machine learning for predictive modeling
 Author

Jahnavi Besabathini