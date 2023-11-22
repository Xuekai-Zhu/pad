def solution():
    
    # Define the cost of the cake and the number of balloons purchased
    CAKE_COST = 11
    BALLOONS_PURCHASED = 12

    # Define the cost of the ice cream and the remaining amount
    ICE_CREAM_COST = 7
    ICE_CREAM_AMOUNT = 2 * ICE_CREAM_COST
    remaining_amount = CAKE_COST + BALLOONS_PURCHASED + ICE_CREAM_AMOUNT

    # Calculate the total amount of money purchased
    total_purchased = CAKE_COST + BALLOONS_PURCHASED + remaining_amount

    # Calculate the amount of money Julia and Nadine received each person
    julia_nadine_allowance = total_purchased / 2

    # Display the amount of money Julia and Nadine received each person
    result = julia_nadine_allowance
    return result

print(solution())