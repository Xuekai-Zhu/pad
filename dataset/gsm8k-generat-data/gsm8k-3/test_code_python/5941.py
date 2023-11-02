def solution():
    """Aunt May milks her cows twice a day. This morning she got 365 gallons of milk. This evening she got 380 gallons. She sold 612 gallons to the local ice cream factory. She had 15 gallons left over from yesterday. How many gallons of milk does she have left?"""
    # Define the total gallons of milk Aunt May got today
    total_milk = 365 + 380

    # Subtract the gallons Aunt May sold to the ice cream factory
    remaining_milk = total_milk - 612

    # Add the gallons Aunt May had left over from yesterday
    remaining_milk += 15

    # Display the remaining gallons of milk
    result = remaining_milk
    return result

print(solution())