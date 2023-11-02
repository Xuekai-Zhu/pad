def solution():
    # Calculate the total amount borrowed
    total_borrowed = 10 * 6  # Shara returned $10 per month for 6 months
    
    # Calculate the amount she still owes after returning half of the money
    still_owed = total_borrowed / 2
    
    # Calculate the remaining amount she will owe in 4 months
    remaining_owed = still_owed - (10 * 4)  # Shara will have returned $10 per month for the next 4 months
    result = remaining_owed
    return result

print(solution())