def solution():
    # Define the number of cows and the amount of milk produced per cow per day
    num_cows = 52
    milk_per_cow_per_day = 1000

    # Calculate the total amount of milk produced per day
    total_milk_per_day = num_cows * milk_per_cow_per_day

    # Calculate the total amount of milk produced per week
    total_milk_per_week = total_milk_per_day * 7

    result = total_milk_per_week
    return result

print(solution())