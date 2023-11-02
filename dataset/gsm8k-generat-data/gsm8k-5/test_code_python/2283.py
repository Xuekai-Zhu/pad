def solution():
    # Count the number of people in each section
    percussion = 1
    brass = 4 + 2 + 1
    strings = 3 + 1 + 1
    woodwinds = 3 + 4
    conductor = 1

    # Calculate the total number of people in the orchestra
    total_people = percussion + brass + strings + woodwinds + conductor
    result = total_people
    return result

print(solution())