def solution():
    # Let's assume Mark had X money when he entered the first store
    starting_money = 0
    found_starting_money = False
    while not found_starting_money:
        # Calculate the remaining money after Mark spent half of it and $14 more
        remaining_money = (starting_money / 2) - 14

        # Calculate the remaining money after Mark spent one-third of his starting money and $16 more
        remaining_money = (2 / 3) * remaining_money - 16

        # Check if Mark has no money left after his spending
        if remaining_money == 0:
            found_starting_money = True
        else:
            starting_money += 1

    result = starting_money
    return result

print(solution())