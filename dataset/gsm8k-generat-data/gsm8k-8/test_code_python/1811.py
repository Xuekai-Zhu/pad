def solution():
    # Determine the total amount of construction paper needed
    total_paper_needed = 8 * 3

    # Determine the total amount of glue needed
    total_glue_needed = 6

    # Determine the total amount of supplies purchased
    total_supplies = total_paper_needed + total_glue_needed

    # Determine the amount of supplies lost
    lost_supplies = total_supplies / 2

    # Determine the amount of supplies left
    remaining_supplies = total_supplies - lost_supplies + 5

    result = remaining_supplies
    return result

print(solution())