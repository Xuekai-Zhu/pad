def solution():
    """John and his best friend Steve bought 12 cupcakes together.  Each cupcake cost $1.50. If they split the costs evenly, how much did each person pay?"""
    # Define the cost per cupcake
    CUPCAKE_COST = 1.50

    # Define the total number of cupcakes purchased
    total_cupcakes = 12

    # Calculate the total cost of all the cupcakes
    total_cost = total_cupcakes * CUPCAKE_COST

    # Calculate the cost per person
    per_person_cost = total_cost / 2

    # Display the cost per person
    result = per_person_cost
    return result

print(solution())