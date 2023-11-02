def solution():
    """Hank is raising money for the local homeless shelter. Hank makes $100 in a carwash and donates 90% of the proceeds to the local homeless shelter. Hank makes $80 in a bake sale and donates 75% of the proceeds to the local homeless shelter. Then he makes $50 mowing lawns and donates 100% of the proceeds to the local homeless shelter. How much money does Hank donate in total?"""
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