def solution():
    starting_cars = 16  # Bobby starts with 16 toy cars
    growth_rate = 0.5  # The number of cars increases by 50% every year
    years = 3  # Bobby wants to know how many cars he will have in 3 years

    # Calculate the number of cars Bobby will have in 3 years
    future_cars = starting_cars * (1 + growth_rate)**years
    result = future_cars
    return result

print(solution())