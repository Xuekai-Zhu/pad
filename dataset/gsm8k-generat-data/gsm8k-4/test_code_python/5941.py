def solution():
    """Aunt May milks her cows twice a day. This morning she got 365 gallons of milk. This evening she got 380 gallons. She sold 612 gallons to the local ice cream factory. She had 15 gallons left over from yesterday. How many gallons of milk does she have left?"""
    # Define the amount of milk Aunt May started with
    starting_milk = 0

    # Calculate the total amount of milk Aunt May has
    total_milk = starting_milk + 365 + 380 + 15

    # Subtract the amount of milk sold to the ice cream factory
    remaining_milk = total_milk - 612

    # return the result
    result = remaining_milk
    return result

print(solution())