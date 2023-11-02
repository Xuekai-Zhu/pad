def solution():
    """At the Taylor family reunion, there were 45 kids and 123 adults. When they sat down to eat, there were 14 tables. How many people sat at each table?"""
    # Define the total number of people
    total_people = 45 + 123

    # Calculate the number of people at each table
    people_per_table = total_people // 14

    # return the result
    result = people_per_table
    return result

print(solution())