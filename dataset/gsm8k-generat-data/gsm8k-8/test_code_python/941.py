def solution():
    # Define the number of grandkids
    num_grandkids = 3

    # Define the number of cards per grandkid and the amount in each card
    num_cards = 2
    card_amount = 80

    # Calculate the total amount given away per year
    total_amount = num_grandkids * num_cards * card_amount
    result = total_amount
    return result

print(solution())