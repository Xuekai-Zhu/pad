def solution():
     max_people = 6
     people_with_dog = 2/3 * max_people
     weight_per_person = 140
     weight_per_dog = weight_per_person / 4
     total_weight = people_with_dog * weight_per_person + weight_per_dog
     result = total_weight
     return result

print(solution())