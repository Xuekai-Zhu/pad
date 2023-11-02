def solution():
    # Calculate the total area of the peanut plantation
    area = 500 * 500  # in square feet

    # Calculate the total weight of peanuts produced in the plantation
    weight_peanuts = area * 50  # in grams

    # Calculate the weight of peanut butter that can be made from the peanuts
    weight_pb = (weight_peanuts / 20) * 5  # in grams

    # Calculate the total revenue from selling the peanut butter
    revenue = (weight_pb / 1000) * 10  # in dollars
    result = revenue
    return result

print(solution())