def solution():
    total_peaches = 18  # The bowl holds 18 peaches in total
    ripe_peaches = 4  # Four of the peaches are ripe initially
    unripe_peaches = total_peaches - ripe_peaches  # The remaining peaches are unripe

    # On each of the first two days, two more peaches ripen
    ripe_peaches += 2 * 2

    # On the third day, three peaches are eaten
    total_peaches -= 3

    # On the fourth and fifth days, two more peaches ripen each day
    ripe_peaches += 2 * 2

    # Calculate the difference between the number of ripe and unripe peaches
    difference = ripe_peaches - (total_peaches - ripe_peaches)

    result = difference
    return result

print(solution())