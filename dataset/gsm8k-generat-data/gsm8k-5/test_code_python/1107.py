def solution():
    starting_amount = 20  # Roman starts with $20 worth of gold coins
    sold_amount = 3  # Roman sells 3 gold coins to Dorothy
    remaining_amount = starting_amount - sold_amount  # Roman has this many gold coins left after selling to Dorothy
    remaining_value = 12  # After selling to Dorothy, Roman has $12 worth of gold coins left

    # Calculate the value of each remaining gold coin
    value_per_coin = remaining_value / remaining_amount

    # Calculate how many gold coins Roman has left
    remaining_coins = (starting_amount - remaining_value) / value_per_coin
    result = remaining_coins
    return result

print(solution())