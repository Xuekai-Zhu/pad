def solution():
    """Mrs. Lim milks her cows twice a day. Yesterday morning, she got 68 gallons of milk and in the evening, she got 82 gallons. This morning, she got 18 gallons fewer than she had yesterday morning. After selling some gallons of milk in the afternoon, Mrs. Lim has only 24 gallons left. How much was her revenue for the milk if each gallon costs $3.50?"""
    morning_yesterday = 68
    evening_yesterday = 82
    morning_today = morning_yesterday - 18
    total_milk = morning_yesterday + evening_yesterday + morning_today
    sold_milk = total_milk - 24
    price_per_gallon = 3.50
    revenue = sold_milk * price_per_gallon
    result = revenue
    return result

print(solution())