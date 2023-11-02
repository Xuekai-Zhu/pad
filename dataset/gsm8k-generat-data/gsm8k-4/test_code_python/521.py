def solution():
    """Micah picks 2 dozen strawberries from the field. He eats 6 and saves the rest for his mom. How many strawberries are there for his mom?"""
    # Define the number of strawberries picked by Micah
    strawberries_picked = 2 * 12

    # Deduct the strawberries that Micah ate
    strawberries_left = strawberries_picked - 6

    # Return the number of strawberries for Micah's mom
    result = strawberries_left
    return result

print(solution())