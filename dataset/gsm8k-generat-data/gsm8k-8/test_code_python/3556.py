def solution():
    # Calculate total savings before expenses
    total_savings = 21 + 46 + 45

    # Subtract expenses from total savings
    total_savings -= 12
    total_savings -= 54

    # Check if total savings is greater than $125
    if total_savings > 125:
        # Add aunt's gift to total savings if applicable
        total_savings += 25

    result = total_savings
    return result

print(solution())