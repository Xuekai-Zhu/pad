def solution():
    
    # Define the cost of bananas per bunch and the number of bunches purchased
    BANANAS_PER_BALL = 4
    BANANAS_PRICE = 0.8
    BUNDS_PURCHASED = 10

    # Calculate the cost of buying bananas individually
    bananas_individual = BANANAS_PER_BALL * BANANAS_PER_BALL

    # Calculate the cost of buying bananas in bunches instead of individually
    bananas_saved = bananas_individual - BANANAS_PRICE

    # Display the amount saved
    result = bananas_saved
    return result

print(solution())