def solution():
    ray_chickens = 10  # Ray took 10 chickens
    mary_chickens = ray_chickens + 6  # Mary took 6 more chickens than Ray
    john_chickens = mary_chickens + 5  # John took 5 more chickens than Mary
    difference = john_chickens - ray_chickens  # Calculate the difference in the number of chickens between John and Ray

    result = difference
    return result

print(solution())