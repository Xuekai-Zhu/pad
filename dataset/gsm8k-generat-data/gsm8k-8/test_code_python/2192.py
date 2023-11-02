def solution():
    # Define the initial donation and the total donation
    initial_donation = 10
    total_donation = initial_donation

    # Iterate through the remaining 4 kilometers
    for i in range(2, 6):
        # Double the previous donation
        current_donation = initial_donation * (2 ** (i - 1))
        # Add the current donation to the total donation
        total_donation += current_donation
    
    result = total_donation
    return result

print(solution())