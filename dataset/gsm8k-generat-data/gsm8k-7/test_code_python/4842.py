def solution():
    lemon_cost = 2
    papaya_cost = 1
    mango_cost = 4
    discount_rate = 0.25
    num_lemons = 6
    num_papayas = 4
    num_mangos = 2

    # Calculate the total cost of all the fruit before discounts
    total_cost_before_discounts = (lemon_cost * num_lemons) + (papaya_cost * num_papayas) + (mango_cost * num_mangos)

    # Calculate the total number of fruits bought, and how many discounts are available
    total_fruits_bought = num_lemons + num_papayas + num_mangos
    num_discounts = total_fruits_bought // 4

    # Calculate the total discount amount
    total_discount_amount = num_discounts * discount_rate

    # Calculate the final cost after discounts
    final_cost = total_cost_before_discounts - total_discount_amount
    result = final_cost
    return result

print(solution())