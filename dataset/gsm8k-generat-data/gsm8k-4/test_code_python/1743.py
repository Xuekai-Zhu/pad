def solution():
    """Wayne wants to serve shrimp cocktail as an appetizer. He plans on 5 shrimp per guest and will have 40 guests. If the shrimp costs $17.00 per pound and each pound has 20 shrimp, how much will he spend on the appetizer?"""
    # Define the number of shrimp per guest and the number of guests
    shrimp_per_guest = 5
    num_guests = 40

    # Calculate the total number of shrimp needed
    total_shrimp = shrimp_per_guest * num_guests

    # Calculate the number of pounds of shrimp needed
    pounds_of_shrimp = total_shrimp / 20

    # Calculate the cost of the shrimp
    cost_of_shrimp = pounds_of_shrimp * 17

    result = cost_of_shrimp
    return result

print(solution())