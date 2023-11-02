def solution():
    """A school is planning a community outreach program. Each classroom must raise $200 for this activity. Classroom A has raised $20 from each of two families, $10 from each of eight families, and $5  from each of ten families. How much more money does Classroom A need in order to reach the goal?"""
    # Define the amount raised from each family group
    group_a = 20
    group_b = 10
    group_c = 5

    # Define the number of families in each group
    num_a = 2
    num_b = 8
    num_c = 10

    # Calculate the total amount raised
    total_raised = (group_a * num_a) + (group_b * num_b) + (group_c * num_c)

    # Calculate the amount still needed to reach the goal
    goal = 200
    still_needed = goal - total_raised

    # Return the result
    result = still_needed
    return result

print(solution())