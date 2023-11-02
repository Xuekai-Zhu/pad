def solution():
    off_the_rack_suit_cost = 300  # The first suit costs $300
    tailored_suit_cost = 3 * off_the_rack_suit_cost + 200  # The second suit costs three times as much plus an extra $200 for tailoring

    # Calculate the total cost of both suits
    total_cost = off_the_rack_suit_cost + tailored_suit_cost
    result = total_cost
    return result

print(solution())