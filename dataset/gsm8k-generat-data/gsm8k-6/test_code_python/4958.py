def solution():
    # Calculate the total number of roses sold
    total_roses = 10 * 12  # 10 bouquets of 12 roses each

    # Calculate the total number of flowers sold in daisy bouquets
    total_daisies = 190 - total_roses  # 190 total flowers minus the number of roses sold

    # Calculate the number of daisies in each daisy bouquet
    daisies_per_bouquet = total_daisies / 10  # 10 daisy bouquets sold
    result = daisies_per_bouquet
    return result

print(solution())