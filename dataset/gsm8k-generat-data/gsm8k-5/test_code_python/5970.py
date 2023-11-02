def solution():
    total_popcorn_needed = 90 + (3*60)  # Jared and his friends need to eat a total of 270 pieces of popcorn
    pieces_per_serving = 30  # There are 30 pieces in a serving

    # Calculate the number of servings needed
    servings_needed = total_popcorn_needed / pieces_per_serving
    result = servings_needed
    return result

print(solution())