def solution():
    num_kids = 45
    num_adults = 123
    num_tables = 14

    # Calculate the total number of people
    total_people = num_kids + num_adults

    # Calculate the number of people seated at each table
    people_per_table = total_people / num_tables
    result = people_per_table
    return result

print(solution())