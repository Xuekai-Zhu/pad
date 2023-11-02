def solution():
    # Define the size of each ad space
    ad_size = 12 * 5

    # Calculate the total number of ad spaces purchased by the three companies
    total_ad_spaces = 10 + 10 + 10

    # Calculate the total square footage of the ad spaces
    total_square_footage = total_ad_spaces * ad_size

    # Calculate the total cost of the ads
    total_cost = total_square_footage * 60

    result = total_cost
    return result

print(solution())