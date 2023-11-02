def solution():
    fritz_money = 40  # Fritz has 40 dollars
    sean_money = (fritz_money / 2) + 4  # Sean has 4 dollars more than half as much money as Fritz
    rick_money = 3 * sean_money  # Rick has 3 times as much money as Sean

    # Calculate the total amount of money that Rick and Sean have
    total_money = rick_money + sean_money
    result = total_money
    return result

print(solution())