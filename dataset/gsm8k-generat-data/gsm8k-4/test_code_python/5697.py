def solution():
    """Neeley bought a loaf of bread from the store and sliced it into 12 pieces. His family ate a third of the bread slices for breakfast. Then Neeley used 2 bread slices to make a sandwich for lunch. How many slices of bread remain?"""
    # Define the total number of bread slices
    total_slices = 12

    # Calculate the number of bread slices eaten for breakfast
    breakfast_slices = total_slices / 3

    # Calculate the remaining number of bread slices
    remaining_slices = total_slices - breakfast_slices - 2

    result = remaining_slices
    return result

print(solution())