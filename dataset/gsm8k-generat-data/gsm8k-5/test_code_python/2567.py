def solution():
    carwash_proceeds = 100  # Hank makes $100 in a carwash
    carwash_donation = 0.9  # Hank donates 90% of the carwash proceeds

    bake_sale_proceeds = 80  # Hank makes $80 in a bake sale
    bake_sale_donation = 0.75  # Hank donates 75% of the bake sale proceeds

    lawn_mowing_proceeds = 50  # Hank makes $50 mowing lawns
    lawn_mowing_donation = 1.0  # Hank donates 100% of the lawn mowing proceeds

    # Calculate the total amount donated
    total_donation = carwash_proceeds * carwash_donation + bake_sale_proceeds * bake_sale_donation + lawn_mowing_proceeds * lawn_mowing_donation
    result = total_donation
    return result

print(solution())