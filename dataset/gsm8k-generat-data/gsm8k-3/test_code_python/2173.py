def solution():
    """At the Taylor family reunion, there were 45 kids and 123 adults. When they sat down to eat, there were 14 tables. How many people sat at each table?"""
    # Calculate the total number of people at the reunion
    total_people = 45 + 123

    # Calculate the average number of people per table
    people_per_table = total_people / 14

    # Round up to the nearest whole number
    people_per_table = math.ceil(people_per_table)

    # Display the number of people per table
    result = people_per_table
    return result

print(solution())