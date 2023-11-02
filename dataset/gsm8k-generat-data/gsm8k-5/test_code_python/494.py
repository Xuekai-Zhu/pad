def solution():
    initial_total_square_footage = 5200 + 7300  # Initial total square footage of both houses
    final_total_square_footage = 16000  # Final total square footage of both houses
    expansion = final_total_square_footage - initial_total_square_footage  # Amount of expansion

    # The smaller house is being expanded
    # Therefore, the amount of expansion is the difference between the new and initial square footage of the smaller house
    # Let X be the amount by which the smaller house is being expanded
    # Then, X + 5200 is the new square footage of the smaller house
    # And, 7300 + (16000 - initial_total_square_footage - X) is the new square footage of the larger house
    # Simplifying the equation, we get:
    # X = 16000 - initial_total_square_footage - 7300 + 5200
    # X = 3500

    smaller_house_expansion = 3500
    result = smaller_house_expansion
    return result

print(solution())