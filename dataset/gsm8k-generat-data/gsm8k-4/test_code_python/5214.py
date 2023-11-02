def solution():
    """Derek was 6 years old when he had three times as many dogs as cars. Ten years later, after selling some of his dogs and buying 210 more cars, the number of cars became twice the number of dogs. How many dogs does Derek have now if he had 90 dogs when he was six years old?"""
    # Define the initial number of dogs and calculate the initial number of cars
    initial_dogs = 90
    initial_cars = initial_dogs / 3

    # Calculate the current number of cars
    current_cars = initial_cars + 210

    # Calculate the current number of dogs
    current_dogs = current_cars / 2

    result = current_dogs
    return result

print(solution())