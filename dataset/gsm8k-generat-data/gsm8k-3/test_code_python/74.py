def solution():
    """Four people lost a total of 103 kilograms of weight. The first person lost 27 kilograms. The second person lost 7 kilograms less than the first person. The two remaining people lost the same amount. How many kilograms did each of the last two people lose?"""
    # Define the weight lost by the first person
    person1_weight = 27

    # Define the weight lost by the second person (7 less than the first person)
    person2_weight = person1_weight - 7

    # Calculate the total weight lost by the last two people
    last2_total_weight = 103 - person1_weight - person2_weight

    # Divide the total weight lost by the last two people equally between them
    last2_weight = last2_total_weight / 2

    result = last2_weight
    return result

print(solution())