def solution():
    """A garden store sells packages of pumpkin seeds for $2.50, tomato seeds for $1.50, and chili pepper seeds for $0.90.
    Harry is planning to plant three different types of vegetables on his farm. How much will Harry have to spend if he wants to
    buy three packets of pumpkin seeds, four packets of tomato seeds, and five packets of chili pepper seeds?"""
    pumpkin_price = 2.5
    tomato_price = 1.5
    chili_price = 0.9

    pumpkin_total = pumpkin_price * 3
    tomato_total = tomato_price * 4
    chili_total = chili_price * 5

    total_cost = pumpkin_total + tomato_total + chili_total
    result = total_cost
    return result

print(solution())