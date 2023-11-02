def solution():
    # Calculate the cost of the glasses
    frames_cost = 200 - 50  # applying the $50 off coupon for frames
    lenses_cost = 500 * 0.2  # applying the 80% insurance coverage for lenses
    total_cost = frames_cost + lenses_cost

    result = total_cost
    return result

print(solution())