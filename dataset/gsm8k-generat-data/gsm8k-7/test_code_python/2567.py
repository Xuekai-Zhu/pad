def solution():
    carwash_proceeds = 100
    carwash_donation = 0.9
    bake_sale_proceeds = 80
    bake_sale_donation = 0.75
    lawn_mowing_proceeds = 50
    lawn_mowing_donation = 1.0

    # Calculate the total amount donated from the carwash
    carwash_donated = carwash_proceeds * carwash_donation

    # Calculate the total amount donated from the bake sale
    bake_sale_donated = bake_sale_proceeds * bake_sale_donation

    # Calculate the total amount donated from lawn mowing
    lawn_mowing_donated = lawn_mowing_proceeds * lawn_mowing_donation

    # Calculate the total amount donated
    total_donated = carwash_donated + bake_sale_donated + lawn_mowing_donated
    result = total_donated
    return result

print(solution())