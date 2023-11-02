def solution():
    num_shirts = 2
    shirt_price = 7

    shoes_price = shirt_price + 3

    bag_price = (num_shirts * shirt_price + shoes_price) / 2

    total_cost = (num_shirts * shirt_price) + shoes_price + bag_price

    result = total_cost
    return result

print(solution())