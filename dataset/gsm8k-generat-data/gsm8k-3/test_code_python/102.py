def solution():
    """Ellie has found an old bicycle in a field and thinks it just needs some oil to work well again. She needs 10ml of oil to fix each wheel and will need another 5ml of oil to fix the rest of the bike. How much oil does she need in total to fix the bike?"""
    # Define the amount of oil needed for each wheel and the rest of the bike
    OIL_PER_WHEEL = 10
    OIL_REST_OF_BIKE = 5

    # Calculate the total amount of oil needed
    total_oil = OIL_PER_WHEEL * 2 + OIL_REST_OF_BIKE

    # Return the result
    result = total_oil
    return result

print(solution())