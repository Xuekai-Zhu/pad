def solution():
    
    carwash_proceeds = 100
    carwash_donation = carwash_proceeds * 0.9
    bake_sale_proceeds = 80
    bake_sale_donation = bake_sale_proceeds * 0.75
    lawn_mowing_proceeds = 50
    lawn_mowing_donation = lawn_mowing_proceeds * 1.0
    total_donation = carwash_donation + bake_sale_donation + lawn_mowing_donation
    result = total_donation
    return result

print(solution())