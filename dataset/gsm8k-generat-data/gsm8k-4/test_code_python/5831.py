def solution():
    """When Herman’s team is busy working on large projects he stops at the drive-through 5 days, every week to buy a breakfast combo for himself and 3 members of his team. Each meal costs $4.00. This current project will last 16 weeks. How much will Herman spend on breakfast?"""
    # Define the cost of each breakfast combo
    combo_cost = 4

    # Define the number of days Herman buys breakfast each week
    breakfast_days = 5

    # Define the number of people Herman buys breakfast for
    breakfast_people = 4

    # Define the number of weeks the project will last
    project_weeks = 16

    # Calculate the total number of breakfast combos Herman buys
    total_combos = breakfast_days * breakfast_people * project_weeks

    # Calculate the total cost of all the breakfast combos
    total_cost = total_combos * combo_cost

    # Return the result
    result = total_cost
    return result

print(solution())