def solution():
    num_people_initial = 40
    cans_initial = 600
    percent_reduction = 30
    num_people_final = num_people_initial - (num_people_initial * percent_reduction / 100)

    # Calculate the number of cans needed to feed the final number of people
    cans_final = (num_people_final * cans_initial) / num_people_initial
    result = cans_final
    return result

print(solution())