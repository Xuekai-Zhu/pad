def solution():
    """Four people lost a total of 103 kilograms of weight. The first person lost 27 kilograms. The second person lost 7 kilograms less than the first person. The two remaining people lost the same amount. How many kilograms did each of the last two people lose?"""
    total_weight_lost = 103
    first_person_weight_lost = 27
    second_person_weight_lost = first_person_weight_lost - 7
    last_two_people_weight_lost = (total_weight_lost - first_person_weight_lost - second_person_weight_lost) / 2
    result = last_two_people_weight_lost
    return result

print(solution())