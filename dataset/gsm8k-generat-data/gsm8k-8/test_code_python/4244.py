def solution():
    # Define the number of chickens Ray took
    ray_chickens = 10

    # Calculate the number of chickens Mary took
    mary_chickens = ray_chickens + 6

    # Calculate the number of chickens John took
    john_chickens = mary_chickens + 5

    # Calculate the difference between John's and Ray's chickens
    difference = john_chickens - ray_chickens
    result = difference
    return result

print(solution())