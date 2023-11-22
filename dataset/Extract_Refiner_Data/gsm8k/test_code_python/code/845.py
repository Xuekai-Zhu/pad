def solution():
    
    # Define the number of eggs and the number of eggs per tray
    eggs = 900
    eggs_per_tray = 30

    # Calculate the total number of trays
    total_trays = eggs // eggs_per_tray

    # Calculate the total earnings
    total_earnings = total_trays * 2.5

    # Display the total earnings
    result = total_earnings
    return result

print(solution())