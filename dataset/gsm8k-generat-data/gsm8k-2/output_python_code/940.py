def solution():
    """Jean has 3 grandchildren. She buys each grandkid 2 cards a year and puts $80 in each card. How much does she give away to grandchildren a year?"""
    num_grandkids = 3
    num_cards_per_grandkid = 2
    amount_per_card = 80
    total_amount_given = num_grandkids * num_cards_per_grandkid * amount_per_card
    result = total_amount_given
    return result

print(solution())