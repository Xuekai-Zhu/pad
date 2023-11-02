def solution():
    # Calculate the cost of buying 3 math textbooks from the school bookshop
    school_cost = 45 * 3

    # Calculate the cost of buying 3 math textbooks from outside bookshops at a 20% discount
    outside_cost = (45 * 0.8) * 3

    # Calculate the amount Peter can save by buying from outside bookshops
    savings = school_cost - outside_cost
    result = savings
    return result

print(solution())