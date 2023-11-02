def solution():
    # Calculate the total revenue for each company
    revenue_A = 4 * 300  # Company A sells 300 big bottles for $4 each
    revenue_B = 3.5 * 350  # Company B sells 350 big bottles for $3.5 each

    # Calculate the difference in revenue between the two companies
    difference = abs(revenue_A - revenue_B)

    result = difference
    return result

print(solution())