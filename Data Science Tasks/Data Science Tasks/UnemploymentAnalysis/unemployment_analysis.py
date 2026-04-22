import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment.csv")

# Set column names manually
df.columns = [
    "Region",
    "Date",
    "Frequency",
    "Estimated Unemployment Rate (%)",
    "Estimated Employed",
    "Estimated Labour Participation Rate (%)",
    "Area"
]

print(df.head())

# Convert date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Remove missing values
df = df.dropna()

# ---- TREND ----
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
plt.title("Unemployment Trend Over Time")
plt.xticks(rotation=45)
plt.show()

# ---- REGION ANALYSIS ----
plt.figure(figsize=(10,5))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.xticks(rotation=90)
plt.title("Unemployment by Region")
plt.show()

# ---- COVID IMPACT ----
covid = df[df['Date'].dt.year == 2020]

plt.figure(figsize=(10,5))
plt.plot(covid['Date'], covid['Estimated Unemployment Rate (%)'], color='red')
plt.title("COVID-19 Impact on Unemployment")
plt.xticks(rotation=45)
plt.show()