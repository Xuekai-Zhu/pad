def solution():
    # Calculate the number of people that can fit in the canoe with the dog
    people_with_dog = (2/3) * 6  

    # Calculate the total weight of people and the dog in the canoe
    total_weight = (people_with_dog * 140) + (0.25 * 140)
    result = total_weight
    return result

print(solution())