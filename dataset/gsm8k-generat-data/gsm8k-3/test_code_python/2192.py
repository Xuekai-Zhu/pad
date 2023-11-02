def solution():
    """Suzanne wants to raise money for charity by running a 5-kilometer race. Her parents have pledged to donate $10 for her first kilometer and double the donation for every successive kilometer. If Suzanne finishes the race, how much money will her parents donate?"""
    # Initialize variables
    current_donation = 10
    total_donation = 0

    # Loop through each kilometer of the race
    for i in range(1, 6):
        # Add the current donation to the total donation
        total_donation += current_donation

        # Double the current donation for the next kilometer
        current_donation *= 2

    # Display the total donation
    result = total_donation
    return result

print(solution())