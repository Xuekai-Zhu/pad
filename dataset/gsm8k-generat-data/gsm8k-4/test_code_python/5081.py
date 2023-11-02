def solution():
    """Penny's canoe can carry 6 people, but if she wants to take her dog, she will only fit 2/3 of that number inside. If every person in a trip where Penny had her dog inside the canoe weighed 140 pounds, and the dog 1/4 as much weight, calculate the total weight the canoe was carrying?"""
    # Define the maximum number of people without the dog
    max_people = 6

    # Define the number of people with the dog
    people_with_dog = int(max_people * (2/3))

    # Define the weight of a person and the weight of the dog
    person_weight = 140
    dog_weight = person_weight / 4

    # Calculate the total weight
    total_weight = (people_with_dog * person_weight) + dog_weight

    return total_weight

print(solution())