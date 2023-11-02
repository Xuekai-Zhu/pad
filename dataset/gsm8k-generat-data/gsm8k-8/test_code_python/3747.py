def solution():
    # Define the prices of each type of calculator
    basic_calculator_price = 8
    scientific_calculator_price = basic_calculator_price * 2
    graphing_calculator_price = scientific_calculator_price * 3

    # Calculate the total cost of each type of calculator
    total_basic_cost = basic_calculator_price * 10
    total_scientific_cost = scientific_calculator_price * 5
    total_graphing_cost = graphing_calculator_price * 3

    # Calculate the total cost of all calculators
    total_cost = total_basic_cost + total_scientific_cost + total_graphing_cost

    # Calculate the change received
    change = 100 - total_cost
    
    result = change
    return result

print(solution())