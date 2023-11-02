def solution():
    georgia_coughs_per_minute = 5
    robert_coughs_per_minute = 2 * georgia_coughs_per_minute

    # Calculate the total number of coughs for Georgia and Robert in 20 minutes
    total_coughs = (georgia_coughs_per_minute + robert_coughs_per_minute) * 20
    
    result = total_coughs
    return result

print(solution())