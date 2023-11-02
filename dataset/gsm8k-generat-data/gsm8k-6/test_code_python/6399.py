def solution():
    fence_length = 500  # meters
    num_fences = 50
    rate = 0.20  # cents per meter

    # Calculate the total amount Emmalyn earned for painting the fences
    total_earned = fence_length * num_fences * rate
    result = total_earned
    return result

print(solution())