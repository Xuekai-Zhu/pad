def solution():
    # Calculate the total monthly cost of the first apartment
    rent_first = 800
    utilities_first = 260
    driving_cost_first = 31 * 20 * 0.58  # 31 miles per day, 20 days per month, $0.58 per mile
    total_first = rent_first + utilities_first + driving_cost_first

    # Calculate the total monthly cost of the second apartment
    rent_second = 900
    utilities_second = 200
    driving_cost_second = 21 * 20 * 0.58  # 21 miles per day, 20 days per month, $0.58 per mile
    total_second = rent_second + utilities_second + driving_cost_second

    # Calculate the difference between the total costs of the two apartments
    difference = total_first - total_second
    result = round(difference)
    return result

print(solution())