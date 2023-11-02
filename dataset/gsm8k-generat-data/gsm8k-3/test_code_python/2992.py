def solution():
    """Wade has called into a rest stop and decides to get food for the road. He buys a sandwich to eat now, one for the road, and one for in the evening. He also buys 2 drinks. If the drinks cost $4 each and Wade spends a total of $26 then how much, in dollars, did the sandwiches each cost?"""
    # Define the cost of each drink
    DRINK_PRICE = 4

    # Define the number of drinks Wade buys
    num_drinks = 2

    # Calculate the total cost of the drinks
    drinks_cost = num_drinks * DRINK_PRICE

    # Calculate the total cost of the sandwiches
    sandwich_cost = 26 - drinks_cost

    # Divide the sandwich cost by the number of sandwiches to get the cost per sandwich
    sandwich_cost_each = sandwich_cost / 3

    # Display the cost per sandwich
    result = sandwich_cost_each
    return result

print(solution())