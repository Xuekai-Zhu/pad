def solution():
    """Jim collects model cars, and he has 301 models total.  Jim has 4 times as many Buicks as Fords, and 3 more than twice the number of Fords than Chevys.  How many Buicks does Jim have?"""
    # Define the total number of models Jim has and the number of Chevys he has
    total_models = 301
    chevy_models = 0

    # Use algebra to solve for the number of Buicks Jim has
    # Let x be the number of Fords
    # Then the number of Buicks is 4x and the number of Chevys is (2x+3)
    # And x + 4x + (2x+3) = 301
    # Simplifying gives x = 49, so Jim has 4x = 196 Buicks
    ford_models = 49
    buick_models = 4 * ford_models

    # Display the number of Buicks Jim has
    result = buick_models
    return result

print(solution())