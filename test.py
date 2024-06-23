import pandas as pd

# Đọc tệp CSV
file_path = r'data/PNJ.csv'
data = pd.read_csv(file_path)

# Chuyển đổi cột 'date' sang định dạng datetime để lọc dữ liệu
data['date'] = pd.to_datetime(data['date'])

# Tạo cột 'month' để nhóm dữ liệu theo tháng
data['month'] = data['date'].dt.to_period('M')

# Lọc dữ liệu trong 6 tháng gần đây
end_date = data['date'].max()
start_date = end_date - pd.DateOffset(months=6)
last_6_months_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

# Danh sách các tháng trong 6 tháng gần đây
months = last_6_months_data['month'].unique()


    
# Tính giá trung bình mua và bán cho từng tháng
monthly_avg_sell = []
for month in months:
    monthly_data = last_6_months_data[last_6_months_data['month'] == month]
    avg_sell = monthly_data['sell'].mean()
    monthly_avg_sell.append(avg_sell)


# Tạo DataFrame để hiển thị bảng dữ liệu trung bình hàng tháng
monthly_avg_df = pd.DataFrame({
    'month': months.astype(str),
    'sell': monthly_avg_sell
})

# Tính giá trung bình mua và bán cho 6 tháng gần đây
average_sell_price = sum(monthly_avg_sell) / len(monthly_avg_sell)

# Tính toán xu hướng thay đổi giá bán trong 6 tháng gần đây
trends_last_6_months = []
for i in range(1, len(monthly_avg_sell)):
    change = ((monthly_avg_sell[i] - monthly_avg_sell[i-1]) / monthly_avg_sell[i-1]) * 100
    trends_last_6_months.append(change)
    print(change)
# Xác định xu hướng tổng thể cho 6 tháng gần đây
if all(change > 0 for change in trends_last_6_months):
    overall_trend_last_6_months = "Tăng"
elif all(change < 0 for change in trends_last_6_months):
    overall_trend_last_6_months = "Giảm"
else:
    overall_trend_last_6_months = "Không ổn định"

# Tính tổng tỷ lệ phần trăm tăng và giảm cho 6 tháng gần đây
increase_percentage_last_6_months = sum(p for p in trends_last_6_months if p > 0)
decrease_percentage_last_6_months = sum(p for p in trends_last_6_months if p < 0)

if increase_percentage_last_6_months > abs(decrease_percentage_last_6_months):
    overall_trend_last_6_months = 'Tăng'
else:
    overall_trend_last_6_months = 'Giảm'

print(monthly_avg_sell)
print(trends_last_6_months)
print("Bảng dữ liệu trung bình hàng tháng:")
print(monthly_avg_df)
print(f"Giá vàng trung bình bán trong 6 tháng gần đây là: {average_sell_price:.2f}")
print(f"Tổng tỷ lệ phần trăm tăng giá theo giá bán: {increase_percentage_last_6_months:.2f}%")
print(f"Tổng tỷ lệ phần trăm giảm giá theo giá bán: {decrease_percentage_last_6_months:.2f}%")
print(f"Xu hướng thay đổi giá vàng theo giá bán trong 6 tháng qua: {overall_trend_last_6_months}")

increase_percentage_last_6_months, decrease_percentage_last_6_months, overall_trend_last_6_months