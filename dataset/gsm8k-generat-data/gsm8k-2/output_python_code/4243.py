def solution():
    """The Grey's bought several chickens at a sale. John took 5 more of the chickens than Mary took. Ray took 6 chickens less than Mary. If Ray took 10 chickens, how many more chickens did John take than Ray?"""
    ray_chickens = 10
    mary_chickens = ray_chickens + 6
    john_chickens = mary_chickens + 5
    difference = john_chickens - ray_chickens
    result = difference
    return result

print(solution())