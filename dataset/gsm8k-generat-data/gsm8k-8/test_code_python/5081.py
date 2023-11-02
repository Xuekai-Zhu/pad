def solution():
    # Calculate the number of people Penny can fit in the canoe with the dog
    canoe_capacity = 6
    dog_capacity = 2/3 * canoe_capacity
    total_capacity = dog_capacity + 1

    # Calculate the total weight of the people and dog
    person_weight = 140
    dog_weight = 1/4 * person_weight
    total_weight = total_capacity * (person_weight + dog_weight)

    result = total_weight
    return result

print(solution())