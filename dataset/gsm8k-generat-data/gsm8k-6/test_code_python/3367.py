def solution():
    # Calculate the number of adult tickets sold
    adult_tickets = 250 - 188  # number of adult tickets sold is the number of total seats minus the number of children

    # Calculate the revenue from adult tickets and child tickets
    adult_revenue = adult_tickets * 6
    child_revenue = 188 * 4
    total_revenue = adult_revenue + child_revenue

    result = total_revenue
    return result

print(solution())