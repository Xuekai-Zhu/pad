def solution():
    total_cost = 65
    current_savings = 35
    additional_money = 20

    # Calculate the total amount of money Gabby has
    total_money = current_savings + additional_money

    # Calculate the amount of money Gabby still needs to save
    remaining_money = total_cost - total_money
    result = remaining_money
    return result

print(solution())