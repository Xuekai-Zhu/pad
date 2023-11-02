def solution():
    # Calculate the average milk production per cow per week
    avg_milk_per_cow = 108/6

    # Calculate the total milk produced in 5 weeks
    total_milk = 2160

    # Calculate the total number of cows
    total_cows = total_milk / (avg_milk_per_cow * 5)
    result = total_cows
    return result

print(solution())