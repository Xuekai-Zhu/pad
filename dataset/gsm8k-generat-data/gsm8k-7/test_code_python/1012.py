def solution():
    house_1_price = 157000
    house_2_price = 499000
    house_3_price = 125000
    commission_rate = 0.02

    # Calculate the commission earned for each house sold
    house_1_commission = house_1_price * commission_rate
    house_2_commission = house_2_price * commission_rate
    house_3_commission = house_3_price * commission_rate

    # Calculate the total commission earned for all three houses
    total_commission = house_1_commission + house_2_commission + house_3_commission
    result = total_commission
    return result

print(solution())