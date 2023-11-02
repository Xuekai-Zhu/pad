def solution():
    # Define the total amount needed and current savings
    total_needed = 5000
    current_savings = 2900

    # Calculate the remaining amount to be saved
    remaining_amount = total_needed - current_savings

    # Calculate the number of months needed to save up remaining amount
    months_needed = remaining_amount / 700

    # Round up to the nearest integer
    months_needed = int(months_needed) + (months_needed % 1 > 0)

    result = months_needed
    return result

print(solution())