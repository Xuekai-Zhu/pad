def solution():
    # Calculate the number of cars that cost less than $15000
    cars_less_15000 = 0.15 * 3000

    # Calculate the number of cars that cost more than $20000
    cars_more_20000 = 0.40 * 3000

    # Calculate the number of cars that cost between $15000 and $20000
    cars_between_15000_20000 = 3000 - cars_less_15000 - cars_more_20000
    result = cars_between_15000_20000
    return result

print(solution())