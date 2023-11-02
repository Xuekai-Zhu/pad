def solution():
    total_cars = 3000
    less_than_fifteen_percent = 0.15
    more_than_twenty_percent = 0.40

    # Calculate the number of cars that cost less than $15000
    less_than_fifteen = total_cars * less_than_fifteen_percent

    # Calculate the number of cars that cost more than $20000
    more_than_twenty = total_cars * more_than_twenty_percent

    # Calculate the number of cars that cost between $15000 and $20000
    between_fifteen_twenty = total_cars - less_than_fifteen - more_than_twenty
    result = between_fifteen_twenty
    return result

print(solution())