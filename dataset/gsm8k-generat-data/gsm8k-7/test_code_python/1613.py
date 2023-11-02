def solution():
    houses_visited_per_day = 50
    percent_buying = 0.2
    percent_buying_half_set = 0.5
    price_half_set = 50
    price_full_set = 150
    num_days_worked_per_week = 5

    # Calculate the number of houses that buy something from John per day
    num_buying_per_day = houses_visited_per_day * percent_buying

    # Calculate the number of houses that buy a half set of knives per day
    num_buying_half_set_per_day = num_buying_per_day * percent_buying_half_set

    # Calculate the number of houses that buy a full set of knives per day
    num_buying_full_set_per_day = num_buying_per_day * percent_buying_half_set

    # Calculate the total amount of money John makes per day
    total_money_per_day = (num_buying_half_set_per_day * price_half_set) + (num_buying_full_set_per_day * price_full_set)

    # Calculate the total amount of money John makes per week
    total_money_per_week = total_money_per_day * num_days_worked_per_week

    result = total_money_per_week
    return result

print(solution())