def solution():
    cost_per_meter = 0.20  # Emmalyn charges 20 cents per meter
    fence_length = 500  # Each fence is 500 meters long
    num_fences = 50  # There are 50 fences in the neighborhood

    # Calculate the total length of all the fences
    total_length = fence_length * num_fences

    # Calculate the total amount Emmalyn earned
    total_earnings = total_length * cost_per_meter
    result = total_earnings
    return result

print(solution())