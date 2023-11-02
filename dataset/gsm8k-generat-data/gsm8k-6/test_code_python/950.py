def solution():
    # Calculate the total earning from stone statues
    stone_earning = 10 * 20  # Theodore can craft 10 stone statues each costing $20
    # Calculate the total earning from wooden statues
    wooden_earning = 20 * 5  # Theodore can craft 20 wooden statues each costing $5
    # Calculate the total earning before taxes
    total_earning = stone_earning + wooden_earning
    # Calculate the amount of taxes to be paid
    taxes = 0.1 * total_earning
    # Calculate the total earning after taxes
    earning_after_taxes = total_earning - taxes
    result = earning_after_taxes
    return result

print(solution())