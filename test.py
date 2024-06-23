import pandas as pd

file_path = (r"C:\Users\admin\Documents\GitHub\GoldPriceVN\data\SJC.csv")
data = pd.read_csv(file_path)
dates = data['date']
buy_prices = data['buy']
sell_prices = data['sell']


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

buy_prices_cleaned = [clean_price(price) for price in buy_prices]
sell_prices_cleaned = [clean_price(price) for price in sell_prices]


trends = []
for i in range(1, len(buy_prices_cleaned)):
    change = ((buy_prices_cleaned[i] - buy_prices_cleaned[i-1]) / buy_prices_cleaned[i-1]) * 100
    trends.append(change)

overall_trend = None
if all(change > 0 for change in trends):
    overall_trend = "Tăng"
elif all(change < 0 for change in trends):
    overall_trend = "Giảm"
else:
    overall_trend = "Không ổn định"

increase_percentage = sum(p for p in trends if p > 0)
decrease_percentage = sum(p for p in trends if p < 0)

print(f"Tổng tỷ lệ phần trăm tăng giá theo giá mua: {increase_percentage:.2f}%")
print(f"Tổng tỷ lệ phần trăm giảm giá theo giá mua: {decrease_percentage:.2f}%")
print(f"Xu hướng thay đổi giá vàng theo giá mua trong 6 tháng qua: {overall_trend}")