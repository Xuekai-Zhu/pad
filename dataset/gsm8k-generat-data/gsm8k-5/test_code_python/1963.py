def solution():
    total_sales = 24000  # Christine sold $24000 worth of items
    commission_rate = 0.12  # Christine gets a 12% commission on all items she sells

    # Calculate Christine's commission earnings
    commission_earnings = total_sales * commission_rate

    # Calculate Christine's total earnings
    total_earnings = commission_earnings * 1.6  # 60% for personal needs, 40% for savings

    # Calculate how much Christine saved
    saved_amount = total_earnings * 0.4

    result = saved_amount
    return result

print(solution())