def solution():
    """Derek was 6 years old when he had three times as many dogs as cars. Ten years later, after selling some of his dogs and buying 210 more cars, the number of cars became twice the number of dogs. How many dogs does Derek have now if he had 90 dogs when he was six years old?"""
    initial_dogs = 90
    initial_age = 6
    ratio = 3
    initial_cars = initial_dogs / ratio
    new_cars = initial_cars + 210
    new_ratio = 2
    new_dogs = new_cars * (new_ratio / (new_ratio + 1))
    result = new_dogs
    return result

print(solution())