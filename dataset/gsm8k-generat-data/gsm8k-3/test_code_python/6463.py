def solution():
    """A toy car factory made 60 cars yesterday. Today, they made twice the number of cars than yesterday. 
    How many toy cars did the factory make?"""
    # Define the number of cars made yesterday
    cars_yesterday = 60

    # Calculate the number of cars made today
    cars_today = cars_yesterday * 2

    # Calculate the total number of cars made
    total_cars = cars_yesterday + cars_today

    # Display the total number of cars made
    result = total_cars
    return result

print(solution())