def solution():
    """Emmalyn decided to paint fences in her neighborhood for twenty cents per meter. If there were 50 fences in the neighborhood that she had to paint and each fence was 500 meters long, calculate the total amount she earned from painting the fences."""
    price_per_meter = 0.2
    num_fences = 50
    fence_length = 500
    total_length = num_fences * fence_length
    earnings = total_length * price_per_meter
    result = earnings
    return result

print(solution())