def solution():
    # Calculate the total number of candies produced in a day
    candies_per_day = 50 * 10  # 50 candies per hour, and the factory works for 10 hours every day
    # Calculate the number of days to produce 4000 candies
    days_to_complete_order = 4000 / candies_per_day
    result = days_to_complete_order
    return result

print(solution())