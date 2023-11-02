def solution():
    chairs_per_row = 6  # There are 6 chairs in each row
    rows = 20  # There are 20 rows of chairs
    people_per_chair = 5  # Each chair holds 5 people

    # Calculate the total number of people who can sit in the chairs
    total_capacity = chairs_per_row * rows * people_per_chair
    result = total_capacity
    return result

print(solution())