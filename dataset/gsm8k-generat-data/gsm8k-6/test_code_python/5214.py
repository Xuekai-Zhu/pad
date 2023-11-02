def solution():
    # Find the number of cars Derek had when he was 6 years old
    num_cars = 90 / 3  # Derek had 3 times as many dogs as cars when he was 6 years old

    # Find the number of cars Derek had 10 years later
    num_cars = num_cars + 210  # Derek bought 210 more cars

    # Find the current number of dogs Derek has
    num_dogs = (num_cars / 2)  # The number of cars is twice the number of dogs

    result = num_dogs
    return result

print(solution())