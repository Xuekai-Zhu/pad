def solution():
    legs_per_person = 2
    legs_per_dog = 4
    legs_per_cat = 4
    num_people = 4
    num_dogs = 2
    num_cats = 1
    total_legs = legs_per_person * num_people + legs_per_dog * num_dogs + legs_per_cat * num_cats
    result = total_legs
    
    return result

print(solution())