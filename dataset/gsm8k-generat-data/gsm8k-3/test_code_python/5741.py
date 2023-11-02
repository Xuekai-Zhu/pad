def solution():
    """Keesha wants to get her hair and nails done for prom.  Hair updos cost $50 and manicures cost $30.  How much will these two services cost her with a 20% tip for each beautician?"""
    # Define the cost of each service
    HAIR_PRICE = 50
    MANICURE_PRICE = 30

    # Define the tip percentage for each service
    TIP_PERCENTAGE = 0.2

    # Calculate the tip for the hair updo
    hair_tip = HAIR_PRICE * TIP_PERCENTAGE

    # Calculate the total cost of the hair updo with tip
    hair_total = HAIR_PRICE + hair_tip

    # Calculate the tip for the manicure
    manicure_tip = MANICURE_PRICE * TIP_PERCENTAGE

    # Calculate the total cost of the manicure with tip
    manicure_total = MANICURE_PRICE + manicure_tip

    # Calculate the total cost of both services with tip
    total_cost = hair_total + manicure_total

    # Display the total cost
    result = total_cost
    return result

print(solution())