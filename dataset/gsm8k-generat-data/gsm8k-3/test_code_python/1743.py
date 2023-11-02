def solution():
    """Wayne wants to serve shrimp cocktail as an appetizer.  He plans on 5 shrimp per guest and will have 40 guests.  If the shrimp costs $17.00 per pound and each pound has 20 shrimp, how much will he spend on the appetizer?"""
    # Define the number of shrimp per guest and the number of guests
    SHRIMP_PER_GUEST = 5
    NUM_GUESTS = 40

    # Calculate the total number of shrimp needed
    total_shrimp = SHRIMP_PER_GUEST * NUM_GUESTS

    # Calculate the number of pounds of shrimp needed
    pounds_of_shrimp = total_shrimp / 20

    # Calculate the cost of the shrimp
    cost_of_shrimp = pounds_of_shrimp * 17.00

    # Display the total cost
    result = cost_of_shrimp
    return result

print(solution())