def solution():
    """Jean has 3 grandchildren. She buys each grandkid 2 cards a year and puts $80 in each card. How much does she give away to grandchildren a year?"""
    # Define the number of grandchildren
    num_grandchildren = 3

    # Define the number of cards per grandchild per year and the value of each card
    num_cards_per_grandchild = 2
    card_value = 80

    # Calculate the total amount of money given to grandchildren per year
    total_money_given = num_grandchildren * num_cards_per_grandchild * card_value

    # return the result
    result = total_money_given
    return result

print(solution())