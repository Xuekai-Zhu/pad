def solution():
    # Calculate the total liters of milk produced by the cows in five weeks
    total_milk = 2160

    # Calculate the average liters of milk produced by a cow per week
    milk_per_cow_weekly = 108

    # Calculate the number of cows on the farm
    num_cows = total_milk / (milk_per_cow_weekly * 5)

    result = num_cows
    return result

print(solution())