def solution():
    """Derek was 6 years old when he had three times as many dogs as cars. Ten years later, after selling some of his dogs and buying 210 more cars, the number of cars became twice the number of dogs. How many dogs does Derek have now if he had 90 dogs when he was six years old?"""
    initial_dogs = 90
    initial_age = 6
    ratio = 3
    cars = initial_dogs // ratio
    dogs = initial_dogs
    age_difference = 10
    cars += 210
    while cars != 2 * dogs:
        age_difference += 1
        if age_difference >= initial_age + 10:
            cars += 1
        dogs -= 1
    result = dogs
    return result

print(solution())