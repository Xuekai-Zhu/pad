def solution():
    """Micah picks 2 dozen strawberries from the field.  He eats 6 and saves the rest for his mom.  How many strawberries are there for his mom?"""
    # Define the number of strawberries in a dozen
    STRAWBERRIES_PER_DOZEN = 12

    # Define the number of dozens of strawberries Micah picked
    dozens_picked = 2

    # Calculate the total number of strawberries Micah picked
    total_picked = dozens_picked * STRAWBERRIES_PER_DOZEN

    # Subtract the number of strawberries Micah ate
    strawberries_for_mom = total_picked - 6

    # Display the number of strawberries for Micah's mom
    result = strawberries_for_mom
    return result

print(solution())