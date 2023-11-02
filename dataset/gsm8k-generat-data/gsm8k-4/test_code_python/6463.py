def solution():
    """A toy car factory made 60 cars yesterday. Today, they made twice the number of cars than yesterday. How many toy cars did the factory make?"""
    # Define the number of cars made yesterday
    yesterday_cars = 60

    # Calculate the number of cars made today
    today_cars = yesterday_cars * 2

    # Calculate the total number of cars made
    total_cars = yesterday_cars + today_cars

    result = total_cars
    return result

print(solution())