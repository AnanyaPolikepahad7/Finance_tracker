# 💸 Personal Finance Tracker with Smart Analytics

A desktop-based Personal Finance Tracker built using **Python (Tkinter)** that allows users to:
- 📥 Log transactions manually or via CSV upload
- 📊 Visualize spending patterns
- 🔍 Detect anomalies in expenses using clustering & Z-score analysis
- 🧠 Get insights into usage categories, accounts, and more

---

## 🚀 Features

- ✅ Add individual transactions using a simple form UI
- 📂 Upload CSV files with bulk transactions
- 📊 Visualizations including:
  - 📌 Category-wise spending clusters
  - 🧾 Account distribution (Pie chart)
  - ⚠️ Anomaly detection (highlighted unusual expenses)
- 👤 User-specific insights (filtered by `User_ID`)
- 🧹 Clean and modular project structure

---




🛠️ How to Use
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/AnanyaPolikepahad7/Finance_tracker.git
cd Finance_tracker
2. Run the App
bash
Copy
Edit
python main.py
3. Enter or Upload Transactions
Use the form UI to manually input transaction data.

Or click Upload CSV to bulk import transactions from a file.

✅ Ensure your CSV contains the following columns:

User_ID,
Date,
Time,
Amount,
Type,
Description,
Merchant,
Category,
Payment Mode,
Account,
Location,
Recurring,




📊 Insights You Get
🔄 Clustering with KMeans to group transaction behavior

⚠️ Anomaly Detection using Z-score (highlighting suspicious spending)

📘 Visuals for:

Category-wise cluster plots

Pie charts by Account or Payment Mode

📌 Notes
The app filters data by User_ID to generate personal insights.

Supported Date Format: YYYY-MM-DD preferred (flexible parsing also supported).

🧠 Built With
🐍 Python 3.x

🎨 Tkinter (UI)

📊 pandas, matplotlib, scikit-learn (for data analysis & visualization)
