def solution():
    """Tony bought 3 lottery tickets and chose identical numbers on each ticket. He finds out that 5 of the numbers on each lottery ticket are winning numbers. If each winning number is worth $20 then how much money, in dollars, has Tony won in total?"""
    # Define the number of winning numbers on each ticket and the value of each winning number
    winning_numbers_per_ticket = 5
    value_per_winning_number = 20

    # Calculate the total number of winning numbers across all tickets
    total_winning_numbers = winning_numbers_per_ticket * 3

    # Calculate the total amount of money won by Tony
    total_winnings = total_winning_numbers * value_per_winning_number

    # return the result
    result = total_winnings
    return result

print(solution())