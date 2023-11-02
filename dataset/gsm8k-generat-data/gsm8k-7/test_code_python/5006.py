def solution():
    num_packs = 3
    total_paid = 20
    change = 11

    # Calculate the total cost of all candy packs
    total_cost = total_paid - change

    # Calculate the price per pack of candy
    price_per_pack = total_cost / num_packs
    result = price_per_pack
    return result

print(solution())