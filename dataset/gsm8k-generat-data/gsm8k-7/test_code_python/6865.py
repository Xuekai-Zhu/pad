def solution():
    smoothie_price = 3
    num_smoothies = 40
    cake_price = 2
    num_cakes = 18

    # Calculate the total amount of money made from selling smoothies
    total_smoothie_money = smoothie_price * num_smoothies

    # Calculate the total amount of money made from selling cakes
    total_cake_money = cake_price * num_cakes

    # Calculate the total amount of money made
    total_money = total_smoothie_money + total_cake_money
    result = total_money
    return result

print(solution())