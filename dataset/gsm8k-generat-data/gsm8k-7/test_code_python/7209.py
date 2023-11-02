def solution():
    cost_of_caramel = 3
    price_of_candy_bar = 2 * cost_of_caramel
    price_of_cotton_candy = price_of_candy_bar / 2

    # Calculate the total cost of 6 candy bars
    total_cost_of_candy_bars = 6 * price_of_candy_bar

    # Calculate the total cost of 3 caramels
    total_cost_of_caramels = 3 * cost_of_caramel

    # Calculate the total cost of 1 cotton candy
    total_cost_of_cotton_candy = price_of_cotton_candy

    # Calculate the total cost of all items
    total_cost = total_cost_of_candy_bars + total_cost_of_caramels + total_cost_of_cotton_candy
    result = total_cost
    return result

print(solution())