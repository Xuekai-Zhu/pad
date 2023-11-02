def solution():
    yesterday_buyers = 50/2  # half the number of buyers yesterday as the day before
    today_buyers = yesterday_buyers + 40  # 40 more buyers in the grocery store today than yesterday
    total_buyers = yesterday_buyers + today_buyers + 50  # total number of buyers in three days
    result = total_buyers
    return result

print(solution())