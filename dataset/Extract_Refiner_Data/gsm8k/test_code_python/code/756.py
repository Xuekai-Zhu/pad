def solution():
    
    # Define the number of people who think horse #2
    horse_2_winners = 50 * 0.2

    # Calculate the number of people who think horse #7
    horse_7_winners = horse_2_winners * 0.6

    # Calculate the number of people who think horse #12
    horse_12_winners = horse_7_winners - horse_2_winners

    # Display the number of people who think horse #12
    result = horse_12_winners
    return result

print(solution())