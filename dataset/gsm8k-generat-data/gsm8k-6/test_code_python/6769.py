def solution():
    # Calculate the number of fish Ken caught and then subtract the number of fish he released
    ken_catch = 2 * 30  
    ken_catch -= 3  # Ken released 3 fish back into the lake

    # Calculate the total number of fish caught by Kendra and Ken
    total_catch = ken_catch + 30 
    result = total_catch
    return result

print(solution())