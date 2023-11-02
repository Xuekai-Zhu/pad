def solution():
    # Calculate the total money earned from recycling bottles
    bottles_money = 80 * 0.10  # Jack gets 10 cents per bottle
    total_money = 15  # Jack made a total of $15 from recycling

    # Calculate the money earned from recycling cans
    cans_money = total_money - bottles_money

    # Calculate the number of cans Jack recycled
    cans_recycled = cans_money / 0.05  # Jack gets 5 cents per can

    result = cans_recycled
    return result

print(solution())