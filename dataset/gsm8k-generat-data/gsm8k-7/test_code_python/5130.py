def solution():
    # weights of Paul's dogs in pounds
    dog_weights = [20, 40, 10, 30, 50]

    # for every 10 pounds, the dogs need 1 pound of dog food per day
    food_per_weight = 1/10

    # calculate the total amount of dog food Paul's dogs need each day
    total_food_per_day = sum(weight * food_per_weight for weight in dog_weights)

    result = total_food_per_day
    return result

print(solution())