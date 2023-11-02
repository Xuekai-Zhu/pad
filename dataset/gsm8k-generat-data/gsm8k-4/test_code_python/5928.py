def solution():
    """Three companies, A, B, and C, each purchased 10 ad spaces on a newspaper, with each ad space having a size of 12 foot by 5-foot rectangle. If each square foot ad was charged at $60, how much money did the three pay for the ads combined?"""
    # Define the dimensions of an ad space
    ad_length = 12
    ad_width = 5

    # Define the number of ad spaces purchased by each company
    company_a_ads = 10
    company_b_ads = 10
    company_c_ads = 10

    # Calculate the total area of all the ad spaces purchased
    total_area = (ad_length * ad_width) * (company_a_ads + company_b_ads + company_c_ads)

    # Calculate the total cost of all the ad spaces
    total_cost = total_area * 60

    # return the result
    result = total_cost
    return result

print(solution())