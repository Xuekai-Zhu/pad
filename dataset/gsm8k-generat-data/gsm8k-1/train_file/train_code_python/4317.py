def solution():
    """Mell went to a cafeteria to spend some time with her friends. She ordered two cups of coffee and one piece of cake. Two of her friends ordered the same, but each of them also bought a bowl of ice cream. One cup of coffee is $4, one piece of cake is $7, and a bowl of ice cream is $3. How much money did Mell and her friends need to pay at the cafeteria?"""
    coffees = 2 + (2 * 2)  # Mell + 2 friends
    cake = 1 + (2 * 1)  # Mell + 2 friends
    ice_cream = 2 * 2  # 2 friends only
    coffee_cost = coffees * 4
    cake_cost = cake * 7
    ice_cream_cost = ice_cream * 3
    total_cost = coffee_cost + cake_cost + ice_cream_cost
    result = total_cost
    return result

print(solution())