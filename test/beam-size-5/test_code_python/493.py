def solution():
    
    # Define the number of days Paul drives his car
    days = 14

    # Define the cost of each morning ride
    morning_cost = 6

    # Define the cost of each afternoon ride
    afternoon_cost = 2

    # Calculate the total cost of driving the car for one day
    daily_cost = days * morning_cost

    # Calculate the total cost of driving the car for one week
    weekly_cost = daily_cost * 7

    # Calculate the total cost of driving the car for two weeks
    total_cost = weekly_cost * 2

    # return the result
    result = total_cost
    return result

print(solution())