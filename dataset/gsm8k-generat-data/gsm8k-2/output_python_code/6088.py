def solution():
    """Javier is having an eating contest with his brother. It's ravioli night and there is meat ravioli, pumpkin ravioli, and cheese ravioli. The meat ravioli weighs 1.5 ounces each. The pumpkin ravioli is 1.25 ounces each. The cheese ravioli is one ounce. Javier eats 5 meat ravioli, 2 pumpkin ravioli, and 4 cheese ravioli. His brother just ate pumpkin ravioli and had 12 of them. What is the total amount of ounces eaten by the winner?"""
    meat_ravioli_weight = 1.5
    pumpkin_ravioli_weight = 1.25
    cheese_ravioli_weight = 1
    javier_meat = 5 * meat_ravioli_weight
    javier_pumpkin = 2 * pumpkin_ravioli_weight
    javier_cheese = 4 * cheese_ravioli_weight
    brother_pumpkin = 12 * pumpkin_ravioli_weight
    javier_total = javier_meat + javier_pumpkin + javier_cheese
    brother_total = brother_pumpkin
    result = max(javier_total, brother_total)
    return result

print(solution())