def solution():
    """Phill had some friends over for pizza. He opens the pizza box and discovers it hasn't been sliced. Phill cuts the pizza in half, and then cuts both halves in half, and then cuts each slice in half again. Phill then passes out 1 slice to 3 of his friends and 2 slices to 2 of his friends. How many slices of pizza are left for Phill?"""
    slices_remaining = 0
    
    # First, we need to calculate how many slices Phill started with
    slices_remaining += 1  # Starting with one unsliced pizza
    slices_remaining *= 2  # Cutting it in half doubles the number of slices
    slices_remaining *= 2  # Cutting both halves in half again doubles the number of slices again
    slices_remaining *= 2  # Cutting each slice in half again doubles the number of slices again
    
    # Next, we need to calculate how many slices Phill gave to his friends
    slices_remaining -= 3  # Phill gave 1 slice to each of 3 friends
    slices_remaining -= 2*2  # Phill gave 2 slices to each of 2 friends
    
    result = slices_remaining
    return result

print(solution())