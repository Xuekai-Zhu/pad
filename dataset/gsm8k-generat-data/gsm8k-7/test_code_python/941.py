def solution():
    num_grandkids = 3
    num_cards_per_grandkid = 2
    money_per_card = 80

    # Calculate the total amount of money Jean gives away to each grandkid per year
    total_money_per_grandkid = num_cards_per_grandkid * money_per_card

    # Calculate the total amount of money Jean gives away to all grandkids per year
    total_money_given = total_money_per_grandkid * num_grandkids
    result = total_money_given
    return result

print(solution())