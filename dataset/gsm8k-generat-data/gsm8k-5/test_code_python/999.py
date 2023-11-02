def solution():
    # Calculate the total amount contributed by the students
    total_contributed = 20 * 5

    # Calculate the total cost of the field trip
    total_cost = 20 * 7

    # Calculate the amount left in the class fund after paying for the field trip
    left_in_fund = 50 + total_contributed - total_cost
    result = left_in_fund
    return result

print(solution())