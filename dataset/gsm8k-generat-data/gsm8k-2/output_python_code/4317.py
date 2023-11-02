def solution():
    """
    Mell went to a cafeteria to spend some time with her friends. She ordered two cups of coffee and one piece of cake.
    Two of her friends ordered the same, but each of them also bought a bowl of ice cream.
    One cup of coffee is $4, one piece of cake is $7, and a bowl of ice cream is $3. How much money did Mell and her friends need to pay at the cafeteria?
    """
    coffee_price = 4
    cake_price = 7
    ice_cream_price = 3
    mell_total = 2*coffee_price + cake_price
    friends_total = mell_total + 2*ice_cream_price
    total = mell_total + friends_total
    result = total
    return result

print(solution())