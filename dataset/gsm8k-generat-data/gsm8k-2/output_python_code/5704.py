def solution():
    """Kiki likes to spend her money on hats and scarves. When she buys twice as many hats as scarves, she spends 60% of her money on hats and the rest on scarves. If she currently has $90, how many scarves will she buy if they are sold at $2 each?"""
    total_money = 90
    hat_percentage = 0.6
    scarf_percentage = 1 - hat_percentage
    hat_price = 0
    scarf_price = 2
    total_hats = 0
    total_scarves = 0
    for i in range(1, 91):
        total_hats = 2 * total_scarves
        hat_price = hat_percentage * total_money / (total_hats + total_scarves)
        if hat_price >= scarf_price:
            total_scarves = i
        else:
            break

    result = total_scarves
    return result

print(solution())