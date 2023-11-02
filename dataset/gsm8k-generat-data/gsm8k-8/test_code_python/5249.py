def solution():
    # Define the number of cakes Ginger makes for each person on each holiday
    child_cakes = 4 * 2  # 2 children, 4 holidays each
    husband_cakes = 7  # 7 holidays for husband
    parent_cakes = 2  # 2 parents, 1 cake each

    # Calculate the total number of cakes made per year and multiply by 10 for 10 years
    total_cakes = (child_cakes + husband_cakes + parent_cakes) * 10
    result = total_cakes
    return result

print(solution())