import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../web_scraping_task/output.csv")

# Clean Price column
df["Price"] = df["Price"].str.replace("Â£", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Remove any missing values in Price
df = df.dropna(subset=["Price"])

# 1. Bar chart of ratings count
rating_counts = df["Rating"].value_counts()

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")
plt.title("Count of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("rating_bar_chart.png")
plt.show()

# 2. Histogram of prices
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_histogram.png")
plt.show()

# 3. Boxplot of prices
plt.figure(figsize=(6, 5))
plt.boxplot(df["Price"])
plt.title("Boxplot of Book Prices")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("price_boxplot.png")
plt.show()

print("Charts created successfully.")