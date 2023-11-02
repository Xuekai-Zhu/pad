def solution():
    """
    A club opens up and charges $20 to enter. James buys 2 rounds for his 5 friends.
    He also buys 6 drinks for himself. Drinks cost $6 each. He decides to eat some food so he orders some fried chicken
    which costs $14. He leaves a 30% tip on everything he orders. How much did he spend for the night?
    """
    entry_fee = 20
    rounds_bought = 2
    friends_bought_for = 5
    drinks_bought = 6
    drink_price = 6
    food_ordered = 14
    tip_percent = 30

    total_spent = (entry_fee + (rounds_bought * friends_bought_for * drink_price) + (drinks_bought * drink_price)
                   + food_ordered)

    tip_amount = total_spent * (tip_percent / 100)
    total_bill = total_spent + tip_amount
    result = total_bill
    return result

print(solution())