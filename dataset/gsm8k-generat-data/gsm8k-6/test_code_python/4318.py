def solution():
    # Calculate the total cost of Mell's order
    mell_order = 2*4 + 7  # Mell ordered two cups of coffee and one piece of cake

    # Calculate the total cost of Mell's friends' orders
    friends_order = 2*(2*4 + 7 + 3)  # Two of Mell's friends ordered the same, but each of them also bought a bowl of ice cream

    # Calculate the total amount of money Mell and her friends need to pay
    total_cost = mell_order + friends_order
    result = total_cost
    return result

print(solution())