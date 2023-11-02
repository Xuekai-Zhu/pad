def solution():
    num_adults = 4
    total_teeth = num_adults * 32

    # Calculate the number of teeth removed for the first person
    first_person_removed = int(total_teeth * 0.25)

    # Calculate the number of teeth removed for the second person
    second_person_removed = int(total_teeth * 0.375)

    # Calculate the number of teeth removed for the third person
    third_person_removed = int(total_teeth * 0.5)

    # Calculate the number of teeth removed for the fourth person
    fourth_person_removed = 4

    # Calculate the total number of teeth removed
    total_removed = first_person_removed + second_person_removed + third_person_removed + fourth_person_removed
    result = total_removed
    return result

print(solution())