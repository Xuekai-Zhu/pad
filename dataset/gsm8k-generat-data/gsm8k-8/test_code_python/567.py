def solution():
    # Calculate the original price for one water bottle
    original_price = 2 / 12

    # Calculate the new price for one water bottle
    new_price = 1.85

    # Calculate the total number of water bottles Lilith had
    total_bottles = 5 * 12

    # Calculate the total amount of money Lilith will receive from selling her water bottles
    total_money = total_bottles * new_price

    # Calculate the amount of money Lilith will have left after buying her friend the birthday gift
    left_money = total_money - 20

    result = left_money
    return result

print(solution())