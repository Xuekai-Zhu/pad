def solution():
    # Define the initial flour amount and flour used on Tuesday
    initial_flour = 500
    tuesday_flour = 240

    # Subtract Tuesday's amount from the initial amount
    remaining_flour = initial_flour - tuesday_flour

    # Calculate the amount spilled and subtract from remaining amount
    spilled_flour = 0.5 * remaining_flour
    remaining_flour -= spilled_flour

    # Calculate the amount needed for a full bag
    needed_flour = initial_flour - remaining_flour
    
    result = needed_flour
    return result

print(solution())