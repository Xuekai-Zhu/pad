def solution():
    capacity = 6  # Penny's canoe can carry 6 people
    dog_capacity = 2/3 * capacity  # If Penny takes her dog, she can only fit 2/3 of the normal number of people
    total_weight = dog_capacity * 140 + 1/4 * 140  # The total weight includes the weight of people and the dog
    result = total_weight
    return result

print(solution())