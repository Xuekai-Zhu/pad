def solution():
    morning_milk = 68  # Mrs. Lim got 68 gallons of milk yesterday morning
    evening_milk = 82  # Mrs. Lim got 82 gallons of milk yesterday evening
    today_morning_milk = morning_milk - 18  # Mrs. Lim got 18 fewer gallons this morning than yesterday morning
    total_milk = morning_milk + evening_milk + today_morning_milk  # Calculate the total amount of milk

    # Calculate the revenue from selling the milk she had left after selling some in the afternoon
    remaining_milk = 24
    revenue = remaining_milk * 3.5

    result = revenue
    return result

print(solution())