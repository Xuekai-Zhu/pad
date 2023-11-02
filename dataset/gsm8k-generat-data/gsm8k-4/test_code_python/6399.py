def solution():
    """Emmalyn decided to paint fences in her neighborhood for twenty cents per meter. If there were 50 fences in the neighborhood that she had to paint and each fence was 500 meters long, calculate the total amount she earned from painting the fences."""
    # Define the price per meter
    PRICE_PER_METER = 0.2

    # Define the number of fences and the length of each fence
    num_fences = 50
    fence_length = 500

    # Calculate the total length of all the fences
    total_length = num_fences * fence_length

    # Calculate the total earnings
    earnings = total_length * PRICE_PER_METER

    # return the result
    result = earnings
    return result

print(solution())