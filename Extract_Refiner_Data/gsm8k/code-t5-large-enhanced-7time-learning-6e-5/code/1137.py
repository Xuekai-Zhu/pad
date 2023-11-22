def solution():
    
    # Define the initial number of eggs and the number of days
    initial_eggs = 3 * 30
    days = 30

    # Define the new number of eggs and the number of days
    new_eggs = 5 * 30
    days = 60

    # Calculate the total number of eggs
    total_eggs = initial_eggs + new_eggs

    # Calculate the number of dozens of eggs needed
    dozens_needed = total_eggs / 12

    # return the result
    result = dozens_needed
    return result

print(solution())