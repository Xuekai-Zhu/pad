def solution():
     """Four people lost a total of 103 kilograms of weight. The first person lost 27 kilograms. The second person lost 7 kilograms less than the first person. The two remaining people lost the same amount. How many kilograms did each of the last two people lose?"""
     first_person = 27
     second_person = first_person - 7
     third_person = second_person - 7
     fourth_person = third_person - 7
     total_weight_lost = first_person + second_person + third_person + fourth_person
     last_two_people = total_weight_lost - (first_person + second_person)
     result = last_two_people / 2
     return result

print(solution())