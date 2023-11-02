def solution():
    num_roses = 40
    num_stolen_roses = 4
    num_people = 9

    # Subtract the stolen roses from the total number of roses
    num_roses_left = num_roses - num_stolen_roses

    # Divide the remaining roses equally among the people
    num_roses_per_person = num_roses_left / num_people
    result = num_roses_per_person
    return result

print(solution())