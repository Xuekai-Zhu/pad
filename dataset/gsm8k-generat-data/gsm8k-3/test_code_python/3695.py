def solution():
    """At the patisserie, a single layer cake slice is $4 and a double layer cake slice is $7.  Dusty buys 7 single layer cake slices and 5 double layer cake slices.  If he pays with a $100 bill, how much change does he receive?"""
    # Define the cost of each type of cake slice
    SINGLE_LAYER_PRICE = 4
    DOUBLE_LAYER_PRICE = 7

    # Define the number of each type of cake slice purchased
    single_layer_slices = 7
    double_layer_slices = 5

    # Calculate the total cost of the single layer cake slices
    single_layer_total = single_layer_slices * SINGLE_LAYER_PRICE

    # Calculate the total cost of the double layer cake slices
    double_layer_total = double_layer_slices * DOUBLE_LAYER_PRICE

    # Calculate the total cost of all the cake slices
    total_cost = single_layer_total + double_layer_total

    # Calculate the change received from the $100 bill
    change = 100 - total_cost

    # Display the change received
    result = change
    return result

print(solution())