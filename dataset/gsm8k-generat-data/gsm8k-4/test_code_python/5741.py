def solution():
    """Keesha wants to get her hair and nails done for prom. Hair updos cost $50 and manicures cost $30. How much will these two services cost her with a 20% tip for each beautician?"""
    # Define the cost of the hair updo and the manicure
    HAIR_COST = 50
    MANICURE_COST = 30

    # Calculate the cost of the hair updo with a 20% tip
    hair_total = HAIR_COST + (HAIR_COST * 0.2)

    # Calculate the cost of the manicure with a 20% tip
    manicure_total = MANICURE_COST + (MANICURE_COST * 0.2)

    # Calculate the total cost of both services
    total_cost = hair_total + manicure_total

    result = total_cost
    return result

print(solution())