def solution():
    num_companies = 3
    num_ad_spaces_per_company = 10
    width = 12  # in feet
    height = 5  # in feet
    cost_per_square_foot = 60  # in dollars

    # Calculate the total area of one ad space
    area_per_ad_space = width * height

    # Calculate the total area of all ad spaces purchased by all companies
    total_area = num_companies * num_ad_spaces_per_company * area_per_ad_space

    # Calculate the total cost of all ads combined
    total_cost = total_area * cost_per_square_foot
    result = total_cost
    return result

print(solution())