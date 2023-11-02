def solution():
    ads_per_company = 10  # Each company purchased 10 ad spaces
    ad_size = 12 * 5  # Each ad space has a size of 12 by 5 feet
    total_ads = ads_per_company * 3  # There are three companies

    # Calculate the total area of all the ads
    total_area = ad_size * total_ads

    # Calculate the total cost of the ads
    total_cost = total_area * 60  # Each square foot ad is charged at $60

    result = total_cost
    return result

print(solution())