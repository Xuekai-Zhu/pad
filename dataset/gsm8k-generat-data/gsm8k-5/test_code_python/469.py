def solution():
    # Calculate the total volume of liquid needed to fill the hot tub in quarts
    total_volume = 40 * 4 * 4  # 40 gallons * 4 quarts per gallon * 4 quarts per bottle

    # Calculate the number of bottles needed, rounding up to the nearest whole number
    num_bottles = math.ceil(total_volume / 4)

    # Calculate the cost of the bottles before the volume discount
    pre_discount_cost = 50 * num_bottles

    # Calculate the discount amount
    discount = 0.2 * pre_discount_cost

    # Calculate the final cost after the discount
    final_cost = pre_discount_cost - discount
    result = final_cost
    return result

print(solution())