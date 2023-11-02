def solution():
    total_money = 240 + 50  # Marta has collected $240 and $50 in tips, for a total of $290
    hourly_rate = 10  # Marta earns $10 per hour

    # Calculate the total number of hours Marta has worked
    total_hours = (total_money / hourly_rate)

    result = total_hours
    return result

print(solution())