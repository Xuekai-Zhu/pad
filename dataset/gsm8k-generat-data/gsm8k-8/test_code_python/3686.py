def solution():
    # Define the amount of money Connie gave to Blake
    give_to_blake = 30000 * 2

    # Calculate the amount of money Connie got from selling the land
    sell_price = give_to_blake * 3

    # Calculate the amount of money Connie initially used to buy the land
    initial_price = sell_price / 2

    # Calculate the amount of money Blake initially gave to Connie
    initial_amount = initial_price - give_to_blake

    result = initial_amount
    return result

print(solution())