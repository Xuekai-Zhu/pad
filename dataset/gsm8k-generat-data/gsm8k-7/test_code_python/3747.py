def solution():
    budget = 100
    basic_calc_price = 8
    scientific_calc_price = basic_calc_price * 2
    graphing_calc_price = scientific_calc_price * 3

    # Calculate the maximum number of basic calculators that can be bought within the budget
    max_basic_calc = budget // basic_calc_price

    # Calculate the maximum number of scientific calculators that can be bought within the budget
    max_scientific_calc = budget // scientific_calc_price

    # Calculate the maximum number of graphing calculators that can be bought within the budget
    max_graphing_calc = budget // graphing_calc_price

    # Calculate the total cost of all calculators
    total_cost = (max_basic_calc * basic_calc_price) + (max_scientific_calc * scientific_calc_price) + (max_graphing_calc * graphing_calc_price)

    # Calculate the change that the math teacher received after buying all calculators
    change = budget - total_cost
    result = change
    return result

print(solution())