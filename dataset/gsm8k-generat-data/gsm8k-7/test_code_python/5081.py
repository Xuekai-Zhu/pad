def solution():
    canoe_capacity = 6
    dog_capacity = canoe_capacity * (2/3)
    total_people = canoe_capacity + dog_capacity
    person_weight = 140
    dog_weight = person_weight * (1/4)

    # Calculate the total weight of people and the dog
    total_weight = (total_people * person_weight) + dog_weight
    result = total_weight
    return result

print(solution())