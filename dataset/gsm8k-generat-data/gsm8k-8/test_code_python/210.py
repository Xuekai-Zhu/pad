def solution():
    # Define the initial number of toy cars and the number of years
    initial_cars = 16
    num_years = 3

    # Calculate the final number of toy cars using the growth formula A = P(1 + r)^t
    final_cars = initial_cars * (1 + 0.5)**num_years

    result = final_cars
    return result

print(solution())