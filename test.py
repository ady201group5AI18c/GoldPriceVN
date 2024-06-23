import pandas as pd

# Load the CSV file
file_path = r'C:\Users\admin\Documents\GitHub\GoldPriceVN\data\PNJ.csv'
data = pd.read_csv(file_path)

# Convert the 'date' column to datetime format for filtering
data['date'] = pd.to_datetime(data['date'])

# Filter data for the last 6 months
end_date = data['date'].max()
start_date = end_date - pd.DateOffset(months=6)
last_6_months_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

# Extract relevant columns for the last 6 months
sell_prices_last_6_months = last_6_months_data['sell']

# Function to clean price strings (remove commas and convert to float)
def clean_price(price):
    if isinstance(price, str):
        try:
            return float(price.replace(',', ''))
        except ValueError:
            return None
    elif isinstance(price, (int, float)):
        return float(price)
    else:
        return None

# Clean buy prices for the last 6 months
sell_prices_cleaned_last_6_months = [clean_price(price) for price in sell_prices_last_6_months]

# Calculate trends based on buy prices for the last 6 months
trends_last_6_months = []
for i in range(1, len(sell_prices_cleaned_last_6_months)):
    change = ((sell_prices_cleaned_last_6_months[i] - sell_prices_cleaned_last_6_months[i-1]) / sell_prices_cleaned_last_6_months[i-1]) * 100
    trends_last_6_months.append(change)

# Determine overall trend for the last 6 months
if all(change > 0 for change in trends_last_6_months):
    overall_trend_last_6_months = "Tăng"
elif all(change < 0 for change in trends_last_6_months):
    overall_trend_last_6_months = "Giảm"
else:
    overall_trend_last_6_months = "Không ổn định"

# Calculate total percentage increase and decrease for the last 6 months
increase_percentage_last_6_months = sum(p for p in trends_last_6_months if p > 0)
decrease_percentage_last_6_months = sum(p for p in trends_last_6_months if p < 0)


print(f"Tổng tỷ lệ phần trăm tăng giá theo giá mua: {increase_percentage_last_6_months:.2f}%")
print(f"Tổng tỷ lệ phần trăm giảm giá theo giá mua: {decrease_percentage_last_6_months:.2f}%")
print(f"Xu hướng thay đổi giá vàng theo giá mua trong 6 tháng qua: {overall_trend_last_6_months}")
print(last_6_months_data)
increase_percentage_last_6_months, decrease_percentage_last_6_months, overall_trend_last_6_months
