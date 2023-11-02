def solution():
    # Define the locations where American football is popular and where the bengal fox is found
    football_popularity = ["United States"]
    bengal_fox_habitat = ["Indian subcontinent"]
    # Check if there is any overlap between the two locations
    overlap = [location for location in football_popularity if location in bengal_fox_habitat]
    if overlap:
        result = "unlikely"
    else:
        result = "no"
    return result

print(solution())