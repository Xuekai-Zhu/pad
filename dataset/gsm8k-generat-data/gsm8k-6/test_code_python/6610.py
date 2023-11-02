def solution():
    eggs_collected = 8 * 2 * 12  # Mortdecai collects 8 dozen eggs every Tuesday and Thursday
    eggs_delivered = 3 * 12 + 5 * 12  # Mortdecai delivers 3 dozen eggs to the market and 5 dozen eggs to the mall
    eggs_used_for_pie = 4 * 12  # Mortdecai uses 4 dozen eggs to make a pie every Saturday
    remaining_eggs = eggs_collected - eggs_delivered - eggs_used_for_pie  # Calculate the remaining eggs
    eggs_donated = remaining_eggs  # Mortdecai donates the remaining eggs to the charity
    result = eggs_donated
    return result

print(solution())