def solution():
    """Penny's canoe can carry 6 people, but if she wants to take her dog, she will only fit 2/3 of that number inside. If every person in a trip where Penny had her dog inside the canoe weighed 140 pounds, and the dog 1/4 as much weight, calculate the total weight the canoe was carrying?"""
    canoe_capacity = 6
    dog_capacity = canoe_capacity * (2/3)
    total_passengers = dog_capacity + 1
    combined_weight = total_passengers * 140
    dog_weight = combined_weight * 0.25
    total_weight = combined_weight + dog_weight
    result = total_weight
    return result

print(solution())