def solution():
    """Tonya is buying Christmas gifts for her sisters. She has 2 sisters and wants to spend the exact same amount on each. She buys her younger sister 4 dolls that cost $15 each. She plans to buy lego sets for her older sister. They cost $20 each. How many lego sets does she buy?"""
    # Define the cost of each doll and Lego set
    DOLL_COST = 15
    LEGO_COST = 20

    # Define the number of sisters
    NUM_SISTERS = 2

    # Calculate the total amount Tonya spent on the dolls
    doll_total = 4 * DOLL_COST

    # Calculate the amount Tonya should spend on each sister
    sister_total = doll_total/NUM_SISTERS

    # Calculate the number of Lego sets Tonya should buy for her older sister
    lego_sets = sister_total/LEGO_COST

    # Display the number of Lego sets Tonya should buy
    result = lego_sets
    return result

print(solution())