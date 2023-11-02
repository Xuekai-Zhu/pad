def solution():
    # Calculate the total cost of buying the items
    total_cost = 3 * 25 + 2 * 75 + 50  # three candy bars cost 3 x 25 = 75 cents, two pieces of chocolate cost 2 x 75 = 150 cents, and one pack of juice costs 50 cents
    quarters_needed = total_cost // 25  # divide the total cost by the value of a quarter (25 cents) and round down to the nearest integer to get the number of quarters needed
    result = quarters_needed
    return result

print(solution())