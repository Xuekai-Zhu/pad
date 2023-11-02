def solution():
    
    carwash_proceeds = 100
    carwash_donation = 0.9 * carwash_proceeds
    bake_sale_proceeds = 80
    bake_sale_donation = 0.75 * bake_sale_proceeds
    lawn_mowing_proceeds = 50
    lawn_mowing_donation = 1.0 * lawn_mowing_proceeds
    total_donation = carwash_donation + bake_sale_donation + lawn_mowing_donation
    result = total_donation
    return result

print(solution())