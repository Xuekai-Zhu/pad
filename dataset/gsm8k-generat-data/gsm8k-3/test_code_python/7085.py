def solution():
    """A school is planning a community outreach program. Each classroom must raise $200 for this activity. Classroom A has raised $20 from each of two families, $10 from each of eight families, and $5  from each of ten families. How much more money does Classroom A need in order to reach the goal?"""
    # Define the amount raised from each type of family
    FAMILY_TYPE_1 = 20
    FAMILY_TYPE_2 = 10
    FAMILY_TYPE_3 = 5

    # Define the number of families in each category
    num_families_type_1 = 2
    num_families_type_2 = 8
    num_families_type_3 = 10

    # Calculate the amount raised from each type of family
    total_raised_type_1 = FAMILY_TYPE_1 * num_families_type_1
    total_raised_type_2 = FAMILY_TYPE_2 * num_families_type_2
    total_raised_type_3 = FAMILY_TYPE_3 * num_families_type_3

    # Calculate the total amount raised by the classroom
    total_raised = total_raised_type_1 + total_raised_type_2 + total_raised_type_3

    # Calculate the amount needed to reach the goal
    goal = 200
    amount_needed = goal - total_raised

    # Display the amount needed to reach the goal
    result = amount_needed
    return result

print(solution())