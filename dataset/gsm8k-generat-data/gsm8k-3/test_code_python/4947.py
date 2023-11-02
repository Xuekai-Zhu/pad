def solution():
    """Tony bought 3 lottery tickets and chose identical numbers on each ticket. He finds out that 5 of the numbers on each lottery ticket are winning numbers. If each winning number is worth $20 then how much money, in dollars, has Tony won in total?"""
    # Define the number of winning numbers on each ticket and the value of each winning number
    WINNING_NUMBERS_PER_TICKET = 5
    WINNING_NUMBER_VALUE = 20

    # Calculate the total number of winning numbers across all 3 tickets
    total_winning_numbers = WINNING_NUMBERS_PER_TICKET * 3

    # Calculate Tony's total winnings
    total_winnings = total_winning_numbers * WINNING_NUMBER_VALUE

    # Display Tony's total winnings
    result = total_winnings
    return result

print(solution())