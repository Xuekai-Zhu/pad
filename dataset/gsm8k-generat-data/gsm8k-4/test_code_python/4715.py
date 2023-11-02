def solution():
    """Mary is paying her monthly garbage bill for a month with exactly four weeks. The garbage company charges Mary $10 per trash bin and $5 per recycling bin every week, and Mary has 2 trash bins and 1 recycling bin. They're giving her an 18% discount on the whole bill before fines for being elderly, but also charging her a $20 fine for putting inappropriate items 
    in a recycling bin. How much is Mary's garbage bill?"""
    # Define the weekly costs for trash and recycling
    trash_cost = 10 * 2
    recycling_cost = 5 * 1

    # Calculate the total cost for the month
    total_cost = (trash_cost + recycling_cost) * 4

    # Apply the discount for being elderly
    total_cost *= 0.82

    # Apply the fine for inappropriate items in recycling bin
    total_cost += 20

    result = total_cost
    return result

print(solution())