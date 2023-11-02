def solution():
    # Calculate the total amount made from selling plain lemonade
    plain_lemonade_total = 36 * 0.75

    # Calculate how much Anna made from selling strawberry lemonade
    strawberry_lemonade_total = 16 - plain_lemonade_total

    # Calculate how much more Anna made from selling plain lemonade than strawberry
    difference = plain_lemonade_total - strawberry_lemonade_total
    result = difference
    return result

print(solution())