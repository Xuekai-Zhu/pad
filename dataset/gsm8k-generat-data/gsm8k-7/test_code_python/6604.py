def solution():
    num_cannoneers = 63
    
    # Calculate the number of women
    num_women = num_cannoneers * 2

    # Calculate the number of men
    num_men = num_women * 2

    # Calculate the total number of people
    total_people = num_cannoneers + num_women + num_men
    result = total_people
    return result

print(solution())