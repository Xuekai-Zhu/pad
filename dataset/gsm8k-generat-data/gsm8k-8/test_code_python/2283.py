def solution():
    # Calculate the total number of people in the brass section
    brass_section = 4 + 2 + 1

    # Calculate the total number of people in the strings section
    strings_section = 3 + 1 + 1

    # Calculate the total number of people in the woodwinds section
    woodwinds_section = 3 + 4

    # Calculate the total number of people in the orchestra
    orchestra_size = brass_section + strings_section + woodwinds_section + 1

    result = orchestra_size
    return result

print(solution())