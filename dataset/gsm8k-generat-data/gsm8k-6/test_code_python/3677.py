def solution():
    # Calculate the number of people who bought pumpkins
    num_people = 96 // 3  # $96 divided by $3 per person

    # Calculate the number of pumpkins remaining after people bought them
    remaining_pumpkins = 83 - num_people

    # Calculate the number of cans of pie filling
    cans_of_pie_filling = remaining_pumpkins // 3

    result = cans_of_pie_filling
    return result

print(solution())