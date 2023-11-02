def solution():
    chairs_per_row = 6
    num_rows = 20
    people_per_chair = 5

    # Calculate the total number of chairs in the church
    total_chairs = chairs_per_row * num_rows

    # Calculate the total number of people who can sit in the chairs
    max_people = total_chairs * people_per_chair

    result = max_people
    return result

print(solution())