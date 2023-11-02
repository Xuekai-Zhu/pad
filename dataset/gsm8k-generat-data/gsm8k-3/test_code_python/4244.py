def solution():
    """The Grey's bought several chickens at a sale. John took 5 more of the chickens than Mary took. Ray took 6 chickens less than Mary. If Ray took 10 chickens, how many more chickens did John take than Ray?"""
    # Define the number of chickens Ray took
    ray_chickens = 10

    # Calculate the number of chickens Mary took
    mary_chickens = ray_chickens + 6

    # Calculate the number of chickens John took
    john_chickens = mary_chickens + 5

    # Calculate the difference between the number of chickens John and Ray took
    difference = john_chickens - ray_chickens

    # Display the difference
    result = difference
    return result

print(solution())