def solution():
    """Tommy has 3 toy cars. His neighbor, Jessie, has 3 cars too. Jessie's older brother has 5 more cars than Tommy and Jessie. How many cars do the three of them have altogether?"""
    # Define the number of cars each person has
    tommy_cars = 3
    jessie_cars = 3
    brother_cars = tommy_cars + jessie_cars + 5

    # Calculate the total number of cars
    total_cars = tommy_cars + jessie_cars + brother_cars

    # Display the total number of cars
    result = total_cars
    return result

print(solution())