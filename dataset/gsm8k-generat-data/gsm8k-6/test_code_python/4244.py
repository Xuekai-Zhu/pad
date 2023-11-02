def solution():
    # Calculate how many chickens Mary took
    mary_chickens = 10 + 6  # Ray took 6 less than Mary, and Ray took 10, so Mary took 10+6=16 chickens

    # Calculate how many chickens John took
    john_chickens = mary_chickens + 5  # John took 5 more chickens than Mary

    # Calculate how many more chickens John took than Ray
    more_chickens = john_chickens - 10  # Ray took 10 chickens, so John took john_chickens - 10 more chickens than Ray

    result = more_chickens
    return result

print(solution())