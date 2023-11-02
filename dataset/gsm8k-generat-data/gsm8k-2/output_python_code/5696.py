def solution():
    """Neeley bought a loaf of bread from the store and sliced it into 12 pieces. His family ate a third of the bread slices for breakfast. Then Neeley used 2 bread slices to make a sandwich for lunch. How many slices of bread remain?"""
    num_slices = 12
    breakfast_slices = num_slices / 3
    lunch_slices = 2
    remaining_slices = num_slices - breakfast_slices - lunch_slices
    result = remaining_slices
    return result

print(solution())