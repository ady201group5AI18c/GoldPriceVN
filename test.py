gold_prices = (r"C:\Users\admin\Documents\GitHub\GoldPriceVN\data\sjc_gold-2024_to_now.csv")

gold_prices_cleaned = []
for price in gold_prices:
    try:
        gold_prices_cleaned.append(float(price.replace(',', '')))
    except ValueError:
        continue  

trends = []
for i in range(1, len(gold_prices_cleaned)):
    change = gold_prices_cleaned[i] - gold_prices_cleaned[i-1]
    trends.append(change)

if all(change > 0 for change in trends):
    overall_trend = "Tăng"
elif all(change < 0 for change in trends):
    overall_trend = "Giảm"
else:
    overall_trend = "Không ổn định"

increase_percentage = sum(p for p in trends if p > 0)
decrease_percentage = sum(p for p in trends if p < 0)

print(f"Tổng tỷ lệ phần trăm tăng giá: {increase_percentage:.2f}%")
print(f"Tổng tỷ lệ phần trăm giảm giá: {decrease_percentage:.2f}%")
print(f"Xu hướng thay đổi giá vàng trong 6 tháng qua: {overall_trend}")
