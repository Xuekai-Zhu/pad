def solution():
    total_gum = 54 + 45  # total pieces of gum
    num_people = 3  # number of people sharing
    pieces_per_person = total_gum // num_people  # integer division to get whole pieces of gum per person
    
    result = pieces_per_person
    return result

print(solution())