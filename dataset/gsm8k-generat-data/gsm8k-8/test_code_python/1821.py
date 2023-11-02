def solution():
    # Calculate the number of students who had their portraits taken before lunch
    before_lunch = 24 / 3

    # Calculate the total number of students who had their portraits taken
    total_taken = before_lunch + 10

    # Calculate the number of students who have not yet had their picture taken
    not_taken = 24 - total_taken
    result = not_taken
    return result

print(solution())