def solution():
    ratio = 10/45  # Ratio of Elsa's coins to Amalie's coins

    # Finding the number of Amalie's coins using the ratio
    total_coins = 440
    amalie_coins = total_coins / (1 + ratio)
    elsa_coins = ratio * amalie_coins

    # Finding the amount Amalie spends on toys
    spent_on_toys = (3/4) * amalie_coins

    # Finding the number of coins Amalie will remain with
    remaining_coins = amalie_coins - spent_on_toys
    result = remaining_coins
    return result

print(solution())