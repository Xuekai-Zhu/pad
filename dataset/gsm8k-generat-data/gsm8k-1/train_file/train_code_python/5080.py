def solution():
    """Penny's canoe can carry 6 people, but if she wants to take her dog, she will only fit 2/3 of that number inside. If every person in a trip where Penny had her dog inside the canoe weighed 140 pounds, and the dog 1/4 as much weight, calculate the total weight the canoe was carrying?"""
    # Calculate the number of people the canoe can carry if the dog is not inside
    max_people_no_dog = 6
    
    # Calculate the number of people the canoe can carry if the dog is inside
    max_people_with_dog = int(max_people_no_dog * 2/3)
    
    # Calculate the weight of each person and the dog
    person_weight = 140
    dog_weight = person_weight * 1/4
    
    # Calculate the total weight the canoe was carrying
    total_weight = max_people_with_dog * person_weight + dog_weight
    
    return total_weight

print(solution())