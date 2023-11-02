def solution():
    original_price_per_head = 600  # $204,000 ÷ 340 = $600 per head
    remaining_cattle = 340 - 172  # 172 cattle died
    lowered_price_per_head = original_price_per_head - 150

    # Calculate the amount the farmer would have made if he sold at the original price
    original_amount = original_price_per_head * remaining_cattle

    # Calculate the amount the farmer would make if he sold at the lowered price
    lowered_amount = lowered_price_per_head * remaining_cattle

    # Calculate the difference between the two amounts
    loss = original_amount - lowered_amount
    result = loss
    return result

print(solution())