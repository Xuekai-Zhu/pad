def solution():
    initial_number_of_cats = 20
    cats_added_on_monday = 2
    cats_added_on_tuesday = 1
    cats_adopted_on_wednesday = 6
    cats_left = initial_number_of_cats + cats_added_on_monday + cats_added_on_tuesday - cats_adopted_on_wednesday
    result = cats_left
    return result

print(solution())