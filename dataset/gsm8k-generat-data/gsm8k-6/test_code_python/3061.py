def solution():
    # Calculate the total number of hours tutored
    total_hours = 35 + 40  # in the second month, she tutored 5 hours more than the first month

    # Calculate the total earnings
    total_earnings = total_hours * 10  # she earns $10 per hour

    # Calculate the amount spent on personal needs
    personal_spending = (4/5) * total_earnings

    # Calculate the amount saved
    savings = total_earnings - personal_spending
    result = savings
    return result

print(solution())