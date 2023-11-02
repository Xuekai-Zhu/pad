def solution():
    # Calculate the original selling price of the cattle
    original_price = 204000 / 340  # $204,000 for 340 cattle

    # Calculate the number of remaining cattle
    remaining_cattle = 340 - 172

    # Calculate the new selling price per head after lowering the price
    new_price = original_price - 150

    # Calculate the total amount the rancher would receive at the lowered price
    lowered_price_total = new_price * remaining_cattle

    # Calculate the total amount the rancher would have received at the original price
    original_price_total = original_price * remaining_cattle

    # Calculate the amount the rancher would lose by selling at the lowered price
    loss = original_price_total - lowered_price_total
    result = loss
    return result

print(solution())