def solution():
    """Mrs. Kaplan has 1/4 as many pizza slices as Bobby has. If Bobby has 2 pizzas and each pizza has 6 slices, how many slices does Mrs. Kaplan have?"""
    
    # Calculate the total number of slices Bobby has
    bobby_slices = 2 * 6

    # Calculate the number of slices Mrs. Kaplan has, which is 1/4 of Bobby's total slices
    kaplan_slices = bobby_slices * 0.25

    #Return the result
    result = kaplan_slices
    return result

print(solution())