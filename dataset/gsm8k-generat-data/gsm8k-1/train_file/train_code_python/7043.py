def solution():
    """Otto’s local kitchen supply store charges $5.00 for the first knife that you need sharpened. They charge $4.00 for the next 3 knives and $3.00 for any knife after that. If Otto has 9 knives that need to be sharpened, how much will it cost to sharpen his knives?"""
    first_knife_cost = 5
    second_to_fourth_knife_cost = 4
    fifth_knife_onward_cost = 3
    num_knives = 9
    total_cost = first_knife_cost + ((min(num_knives - 1, 3)) * second_to_fourth_knife_cost) + ((max(num_knives - 4, 0)) * fifth_knife_onward_cost)
    result = total_cost
    return result

print(solution())