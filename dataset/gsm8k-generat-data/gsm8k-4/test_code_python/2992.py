def solution():
    """Wade has called into a rest stop and decides to get food for the road. He buys a sandwich to eat now, one for the road, and one for in the evening. He also buys 2 drinks. If the drinks cost $4 each and Wade spends a total of $26 then how much, in dollars, did the sandwiches each cost?"""
    # Define the number of drinks and the cost per drink
    num_drinks = 2
    drink_cost = 4

    # Define the total cost of the drinks
    total_drinks_cost = num_drinks * drink_cost

    # Define the total cost of the sandwiches
    total_sandwich_cost = 26 - total_drinks_cost

    # Define the cost per sandwich
    sandwich_cost = total_sandwich_cost / 3

    result = sandwich_cost
    return result

print(solution())