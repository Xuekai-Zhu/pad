def solution():
    """Hank is raising money for the local homeless shelter. Hank makes $100 in a carwash and donates 90% of the proceeds to the local homeless shelter. Hank makes $80 in a bake sale and donates 75% of the proceeds to the local homeless shelter. Then he makes $50 mowing lawns and donates 100% of the proceeds to the local homeless shelter. How much money does Hank donate in total?"""
    # Calculate the donation from the carwash
    carwash_donation = 100 * 0.9

    # Calculate the donation from the bake sale
    bake_sale_donation = 80 * 0.75

    # Calculate the donation from mowing lawns
    mowing_donation = 50 * 1

    # Calculate the total donation
    total_donation = carwash_donation + bake_sale_donation + mowing_donation

    result = total_donation
    return result

print(solution())