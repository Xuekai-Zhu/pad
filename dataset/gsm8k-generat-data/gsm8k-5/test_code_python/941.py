def solution():
    num_grandkids = 3  # Jean has 3 grandchildren
    cards_per_grandkid = 2  # Jean buys 2 cards for each grandkid
    money_per_card = 80  # Jean puts $80 in each card

    # Calculate the total amount of money Jean gives away to grandchildren per year
    total_money = num_grandkids * cards_per_grandkid * money_per_card
    result = total_money
    return result

print(solution())