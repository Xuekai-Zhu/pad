def solution():
    peanuts_per_second = 20 / 15
    peanuts_per_minute = peanuts_per_second * 60
    total_peanuts = peanuts_per_minute * 6
    result = total_peanuts
    return result

Question: Jennie has $100. She spends $8 per day. How many days will it take her to spend all her money?
Solution:
def solution():
    initial_amount = 100
    amount_spent_per_day = 8
    days_until_broke = initial_amount / amount_spent_per_day
    result = days_until_broke
    return result

print(solution())