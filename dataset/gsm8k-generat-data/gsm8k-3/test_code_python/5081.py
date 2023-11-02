def solution():
    """Penny's canoe can carry 6 people, but if she wants to take her dog, she will only fit 2/3 of that number inside. If every person in a trip where Penny had her dog inside the canoe weighed 140 pounds, and the dog 1/4 as much weight, calculate the total weight the canoe was carrying?"""
    # Define the maximum number of people Penny's canoe can carry
    MAX_PEOPLE = 6

    # Determine the maximum number of people Penny can take with her dog inside
    max_people_with_dog = int(MAX_PEOPLE * (2/3))

    # Calculate the weight of the dog
    dog_weight = (1/4) * 140

    # Calculate the weight of the people
    people_weight = max_people_with_dog * 140

    # Calculate the total weight the canoe was carrying
    total_weight = dog_weight + people_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())