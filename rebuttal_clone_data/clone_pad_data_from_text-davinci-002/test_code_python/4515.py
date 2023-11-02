def solution():
     charge_per_kilo = 2
     kilos_washed_2_days_ago = 5
     kilos_washed_1_day_ago = kilos_washed_2_days_ago + 5
     kilos_washed_today = kilos_washed_1_day_ago * 2
     total_kilos_washed = kilos_washed_2_days_ago + kilos_washed_1_day_ago + kilos_washed_today
     total_earnings = total_kilos_washed * charge_per_kilo
     result = total_earnings
     return result

print(solution())