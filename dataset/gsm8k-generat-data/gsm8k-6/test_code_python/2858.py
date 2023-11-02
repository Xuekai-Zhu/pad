def solution():
    # Calculate the number of women and children at the party
    women = 60/2
    children = 60 - (women + 15)

    # Calculate the number of men who left during the celebration
    men_left = 15/3 

    # Calculate the number of children who left during the celebration
    children_left = 5 

    # Calculate the number of people who stayed and enjoyed the celebration
    total_people_stayed = women + (15 - men_left) + (children - children_left)

    result = total_people_stayed
    return result

print(solution())