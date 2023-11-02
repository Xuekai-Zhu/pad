def solution():
    # Calculate total savings
    total_savings = 50 + 37 + 11  # $50 in September, $37 in October, $11 in November

    # Check if Lindsey saved more than $75 to receive the bonus
    if total_savings > 75:
        total_savings += 25  # Add $25 bonus to total savings

    # Subtract money spent on video game
    total_savings -= 87

    result = total_savings
    return result

print(solution())