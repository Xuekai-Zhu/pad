def solution():
    # Calculate the total number of popcorn pieces that all four friends can eat
    total_popcorn_pieces = 90 + 60*3
    # Calculate the number of servings needed, rounding up to the nearest whole number
    servings_needed = math.ceil(total_popcorn_pieces/30)
    result = servings_needed
    return result

print(solution())