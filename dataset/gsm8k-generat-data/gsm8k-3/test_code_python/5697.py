def solution():
    """Neeley bought a loaf of bread from the store and sliced it into 12 pieces. His family ate a third of the bread slices for breakfast. Then Neeley used 2 bread slices to make a sandwich for lunch. How many slices of bread remain?"""
    # Define the number of bread slices
    bread_slices = 12

    # Calculate the number of bread slices eaten for breakfast
    breakfast_slices = bread_slices // 3

    # Calculate the number of bread slices remaining after breakfast
    bread_slices -= breakfast_slices

    # Calculate the number of bread slices used for lunch
    lunch_slices = 2

    # Calculate the number of bread slices remaining after lunch
    bread_slices -= lunch_slices

    # Display the number of bread slices remaining
    result = bread_slices
    return result

print(solution())