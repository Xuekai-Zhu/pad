def solution():
    
    # Calculate the total cost of raising the child from age 0 to 8
    cost_first_eight_years = 8 * 10000

    # Calculate the total cost of raising the child from age 9 to 18
    cost_next_nine_years = 9 * 20000

    # Calculate the total cost of university tuition
    cost_university = 250000

    # Calculate the total cost of raising the child
    total_cost = (cost_first_eight_years + cost_next_nine_years + cost_university) / 0.5
    result = total_cost
    return result

print(solution())