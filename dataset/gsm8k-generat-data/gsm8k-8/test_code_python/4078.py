def solution():
    # Calculate the number of girls at the beginning of the year
    initial_girls = round(15 * 1.2)

    # Calculate the total number of students at the beginning of the year
    initial_total = initial_girls + 15

    # Calculate the new number of girls
    new_girls = initial_girls * 2

    # Calculate the new total number of students
    new_total = new_girls + 15

    # Calculate the final result
    result = new_total
    
    return result

print(solution())