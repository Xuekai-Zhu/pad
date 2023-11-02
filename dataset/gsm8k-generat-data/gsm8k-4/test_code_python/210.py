def solution():
    """Bobby has 16 toy cars, and the number of cars he has increases by 50% every year. How many toy cars will Bobby have in three years?"""
    # Define the initial number of toy cars
    initial_cars = 16
    
    # Calculate the number of toy cars Bobby will have after 3 years
    final_cars = initial_cars * (1.5 ** 3)
    
    result = round(final_cars)
    return result

print(solution())