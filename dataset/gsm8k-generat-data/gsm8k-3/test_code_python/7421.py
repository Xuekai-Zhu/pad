def solution():
    """A Senior Center is hosting a bingo night. $2,400 in prize money will be given away. The first winner of the night will receive a third of the money. The next ten winners will each receive a 10th of the remaining amount. How many dollars will each of the next ten winners receive?"""
    # Define the total prize money and calculate the amount for the first winner
    prize_money = 2400
    first_winner_amount = prize_money // 3

    # Calculate the remaining amount after the first winner
    remaining_amount = prize_money - first_winner_amount

    # Calculate the amount for each of the next ten winners
    next_ten_winners_amount = remaining_amount // 10

    # Display the amount for each of the next ten winners
    result = next_ten_winners_amount
    return result

print(solution())