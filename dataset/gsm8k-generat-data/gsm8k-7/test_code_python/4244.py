def solution():
    ray_chickens = 10
    mary_chickens = ray_chickens + 6  # Mary took 6 more than Ray
    john_chickens = mary_chickens + 5  # John took 5 more than Mary
    john_extra_chickens = john_chickens - ray_chickens  # Calculate the difference in chickens taken between John and Ray
    result = john_extra_chickens
    return result

print(solution())