def solution():
    # Calculate the total amount spent by Abraham
    total_spent = 4 * 4 + 3 + 30  # Abraham bought 4 shower gels for $4 each, a tube of toothpaste for $3, and had $30 remaining in his budget
    remaining_budget = 60 - total_spent  # Calculate the remaining budget after deducting the amount spent
    spent_on_detergent = remaining_budget  # The amount spent on the detergent is equal to the remaining budget
    result = spent_on_detergent
    return result

print(solution())