def solution():
    adults = 10
    children = 11
    adult_price = 8
    total_price = 124

    # Calculate the total cost of adult tickets
    adult_total = adults * adult_price

    # Calculate the cost of children's tickets
    children_price = (total_price - adult_total) / children
    result = children_price
    return result

print(solution())