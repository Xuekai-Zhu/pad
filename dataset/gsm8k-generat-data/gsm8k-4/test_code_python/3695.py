def solution():
    """At the patisserie, a single layer cake slice is $4 and a double layer cake slice is $7. Dusty buys 7 single layer cake slices and 5 double layer cake slices. If he pays with a $100 bill, how much change does he receive?"""
    # Define the price of a single layer cake and a double layer cake
    single_layer_price = 4
    double_layer_price = 7

    # Calculate the total cost of the single layer cake slices
    single_layer_cost = single_layer_price * 7

    # Calculate the total cost of the double layer cake slices
    double_layer_cost = double_layer_price * 5

    # Calculate the total cost of all the cake slices
    total_cost = single_layer_cost + double_layer_cost

    # Calculate the change received from a $100 bill
    change = 100 - total_cost
    result = change
    return result

print(solution())