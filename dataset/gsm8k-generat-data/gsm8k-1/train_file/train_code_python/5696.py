def solution():
    """
    Neeley bought a loaf of bread from the store and sliced it into 12 pieces. 
    His family ate a third of the bread slices for breakfast. 
    Then Neeley used 2 bread slices to make a sandwich for lunch. 
    How many slices of bread remain?
    """
    total_slices = 12
    slices_for_breakfast = total_slices // 3
    slices_for_lunch = 2
    slices_remaining = total_slices - slices_for_breakfast - slices_for_lunch
    result = slices_remaining
    return result

print(solution())