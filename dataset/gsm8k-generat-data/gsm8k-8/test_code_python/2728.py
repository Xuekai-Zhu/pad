def solution():
    # Calculate the value of one head of cattle
    original_price = 204000 / 340

    # Calculate the number of healthy cattle remaining after the sickness
    remaining_cattle = 340 - 172

    # Calculate the amount the rancher would make by selling the remaining cattle at the original price
    original_sale_price = original_price * remaining_cattle

    # Calculate the amount the rancher would make by selling the remaining cattle at the lowered price
    lowered_price = original_price - 150
    lowered_sale_price = lowered_price * remaining_cattle

    # Calculate the difference between the two sale prices
    difference = original_sale_price - lowered_sale_price
    result = difference
    return result

print(solution())