def solution():
    # Set the cost of each scarf
    scarf_cost = 2

    # Set Kiki's total amount of money
    total_money = 90

    # Calculate the amount Kiki spends on hats
    hat_percentage = 0.6
    hat_money = total_money * hat_percentage

    # Calculate the amount Kiki spends on scarves
    scarf_money = total_money - hat_money

    # Calculate the number of scarves Kiki can buy
    hat_to_scarf_ratio = 2
    num_scarves = scarf_money / (scarf_cost * (1 + hat_to_scarf_ratio))
    result = num_scarves
    return result

print(solution())