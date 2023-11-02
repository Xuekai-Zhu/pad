def solution():
    number_of_saved_people = 144000
    number_of_residents_in_LA = 10000000
    if number_of_residents_in_LA > number_of_saved_people:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())