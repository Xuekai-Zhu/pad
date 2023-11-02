def solution():
    # Calculate the total amount of money raised in the first 3 days
    total_first_3_days = 600 + 900 + 400  

    # Calculate the total amount of money raised in the next 4 days
    total_next_4_days = (total_first_3_days / 2) * 4  

    # Calculate the total amount of money raised by the group
    total_amount = total_first_3_days + total_next_4_days  

    # Calculate the total amount needed for the trip
    total_needed = 6 * 450 + 3000  

    # Calculate the remaining amount needed by each person
    remaining_amount = (total_needed - total_amount) / 6  

    result = remaining_amount
    return result

print(solution())