def solution():
    # Calculate the total number of candies Lisa eats per week
    candies_per_week = 5*1 + 2*2  # Lisa eats 1 candy per day on 5 days and 2 candies per day on 2 days

    # Calculate the number of weeks it takes for Lisa to eat all the candies
    weeks_to_finish = 36 / candies_per_week

    result = weeks_to_finish
    return result

print(solution())