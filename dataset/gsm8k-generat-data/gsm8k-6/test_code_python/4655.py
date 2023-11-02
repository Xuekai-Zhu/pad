def solution():
    # Convert 7.5 hours to minutes
    total_minutes = 7.5 * 60

    # Subtract the minutes that Adah practiced on the 2 days
    remaining_minutes = total_minutes - (86*2)

    result = remaining_minutes
    return result

print(solution())