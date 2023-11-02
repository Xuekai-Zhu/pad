def solution():
    num_adults = 400
    num_children = 200
    total_people = num_adults + num_children
    total_collected = 16000

    # Let x be the price of a child's ticket
    # The price of an adult's ticket is then 2x
    # We can set up the equation:
    # num_adults * 2x + num_children * x = total_collected
    # Simplifying, we get:
    # 400 * 2x + 200 * x = 16000
    # 800x + 200x = 16000
    # 1000x = 16000
    # x = 16

    child_price = 16
    adult_price = 2 * child_price
    result = adult_price
    return result

print(solution())