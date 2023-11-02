def solution():
    num_puppies = 7
    num_portions = 105
    num_days = 5

    # Calculate the total number of portions each puppy needs per day
    total_portions_per_day = num_portions / (num_days * num_puppies)

    result = total_portions_per_day
    return result

print(solution())