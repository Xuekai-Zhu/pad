def solution():
    ratio = 10 / 45
    total_coins = 440

    # Calculate the number of coins Elsa has
    elsa_coins = total_coins / (1 + ratio)
    # Calculate the number of coins Amalie has
    amalie_coins = total_coins - elsa_coins

    # Calculate how much Amalie spent on toys
    spent_on_toys = amalie_coins * (3 / 4)

    # Calculate how many coins Amalie will have left
    remaining_coins = amalie_coins - spent_on_toys
    result = remaining_coins
    return result

print(solution())