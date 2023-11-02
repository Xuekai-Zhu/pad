def solution():
    # Use algebra to solve the problem:
    # Let x be the number of adults and 3x be the number of children
    # 7x + 3(3x) = 6000
    # 16x = 6000
    # x = 375
    # So there were 375 adults and 1125 children
    # The total number of people who bought tickets is 1500

    num_adults = 375  
    num_children = 3 * num_adults
    total_people = num_adults + num_children
    result = total_people
    return result

print(solution())