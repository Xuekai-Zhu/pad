def solution():
    candies_per_hour = 50  # The factory produces 50 candies per hour
    total_candies = 4000  # The factory needs to fulfill an order of 4000 candies
    hours_per_day = 10  # The factory works for 10 hours per day

    # Calculate the total number of hours required to fulfill the order
    total_hours = total_candies / candies_per_hour

    # Calculate the number of days required to fulfill the order
    total_days = total_hours / hours_per_day
    result = total_days
    return result

print(solution())