def solution():
    """One of Robi's new year's resolutions is to start saving. He started to save $2 in January. This is followed by $4 in February and $8 in March. If he continues this saving pattern, how much will be his total savings after 6 months?"""
    # Initialize total savings
    total_savings = 2 + 4 + 8

    # Loop through the remaining 3 months
    for i in range(3, 7):
        # Calculate the next month's savings
        savings = 2 ** (i - 1)

        # Add the next month's savings to the total
        total_savings += savings

    # Display the total savings after 6 months
    result = total_savings
    return result

print(solution())