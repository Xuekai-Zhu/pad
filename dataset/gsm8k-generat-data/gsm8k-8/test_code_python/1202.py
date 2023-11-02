def solution():
    # Calculate driving-related costs for the first apartment
    first_apartment_driving_cost = 31 * 0.58 * 20
    # Calculate total monthly cost for the first apartment
    first_apartment_total_cost = 800 + 260 + first_apartment_driving_cost

    # Calculate driving-related costs for the second apartment
    second_apartment_driving_cost = 21 * 0.58 * 20
    # Calculate total monthly cost for the second apartment
    second_apartment_total_cost = 900 + 200 + second_apartment_driving_cost

    # Calculate the difference in total monthly costs
    difference = round(second_apartment_total_cost - first_apartment_total_cost)
    result = difference
    return result

print(solution())