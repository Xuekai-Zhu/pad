def solution():
    sandwich_price = 0.30
    juice_price = 0.20
    total_money = 2.50

    # Calculate the total cost of one sandwich and one pack of juice
    item_cost = sandwich_price + juice_price

    # Calculate the number of friends that Lyle can buy for
    num_friends = int((total_money - item_cost) / item_cost)
    result = num_friends
    return result

print(solution())