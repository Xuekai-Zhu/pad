def solution():
    # Define variables for the number of CDs and their prices
    the_dark_cds = 2
    avn_cd_price = 12
    the_dark_cd_price = avn_cd_price * 2
    ninety_cds_price = 0.4 * (the_dark_cds * the_dark_cd_price + avn_cd_price)

    # Calculate the total cost
    total_cost = (the_dark_cds * the_dark_cd_price) + avn_cd_price + (5 * ninety_cds_price)

    result = total_cost
    return result

print(solution())