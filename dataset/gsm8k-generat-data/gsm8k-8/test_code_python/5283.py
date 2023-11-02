def solution():
    # Calculate the amount of taxes
    taxes = 0.05 * 40

    # Calculate the total cost before discount
    total_cost_before_discount = 40 + taxes

    # Calculate the final cost after discount
    final_cost_after_discount = total_cost_before_discount - 8

    # Calculate how much each person pays
    cody_pays = final_cost_after_discount / 2
    result = cody_pays
    return result

print(solution())