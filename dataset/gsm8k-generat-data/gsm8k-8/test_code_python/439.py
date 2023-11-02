def solution():
    # Define the cost of each item
    tshirt_cost = 8
    keychain_cost = 2 / 3
    bag_cost = 10

    # Calculate the total cost of the t-shirts and bags Timothy wants to buy
    total_cost = 2 * tshirt_cost + 2 * bag_cost

    # Calculate the amount of money left after buying the t-shirts and bags
    money_left = 50 - total_cost

    # Calculate how many keychains Timothy can buy with the money left
    keychain_count = int(money_left // keychain_cost)

    result = keychain_count
    return result

print(solution())