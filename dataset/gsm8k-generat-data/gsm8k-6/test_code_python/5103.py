def solution():
    # Calculate the number of hot dogs eaten by the 2nd competitor
    hotdogs_2nd = 2 * 12  # 2nd competitor ate twice as much as the 1st competitor

    # Calculate the number of hot dogs eaten by the 3rd competitor
    hotdogs_3rd = hotdogs_2nd * 0.75  # 3rd competitor ate 25% less than the 2nd competitor
    result = hotdogs_3rd
    return result

print(solution())