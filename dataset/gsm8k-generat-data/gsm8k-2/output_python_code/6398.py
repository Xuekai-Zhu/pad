def solution():
    """Emmalyn decided to paint fences in her neighborhood for twenty cents per meter. If there were 50 fences in the neighborhood that she had to paint and each fence was 500 meters long, calculate the total amount she earned from painting the fences."""
    price_per_meter = 0.20
    fence_length = 500
    num_fences = 50
    total_length = fence_length * num_fences
    total_earnings = total_length * price_per_meter
    result = total_earnings
    return result

print(solution())