def solution():
    growth_rate = 2  # The tree grows 2 feet per week
    starting_height = 10  # The tree is currently 10 feet tall
    weeks_in_month = 4  # There are 4 weeks in a month
    months = 4  # Josue wants to know the tree's total height after 4 months

    # Calculate the total growth in feet over 4 months
    total_growth = growth_rate * weeks_in_month * months

    # Calculate the tree's final height after 4 months
    final_height = starting_height + total_growth
    result = final_height
    return result

print(solution())