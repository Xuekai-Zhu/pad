def solution():
    # Calculate the total area of the peanut plantation
    area = 500 * 500
    # Calculate the total number of square feet of peanuts
    num_peanut_sqft = area
    # Calculate the total number of grams of peanuts
    total_peanuts = num_peanut_sqft * 50
    # Calculate the total number of grams of peanut butter that can be made
    total_peanut_butter = total_peanuts / 20 * 5
    # Calculate the total number of kg of peanut butter that can be made
    total_kg_peanut_butter = total_peanut_butter / 1000
    # Calculate the total revenue from selling the peanut butter
    total_revenue = total_kg_peanut_butter * 10
    result = total_revenue
    return result

print(solution())