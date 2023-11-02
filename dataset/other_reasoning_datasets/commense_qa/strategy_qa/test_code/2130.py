def solution():
    # Define the time period when pasteurization was introduced and the shelf life of eggs with their bloom intact
    pasteurization_introduced = 1990
    bloom_intact_shelf_life = "one month"
    # Check if eggs needed to be kept cold before pasteurization was introduced
    if pasteurization_introduced > 1500:
        result = "no"  # Refrigeration was not widely available before the 20th century
    else:
        result = "yes"
    return result

print(solution())