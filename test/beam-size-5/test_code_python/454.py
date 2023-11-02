def solution():
    jennifer_puppies = 8
    jennifer_spots = 3

    brandon_puppies = 12
    brandon_spots = 4

    # Calculate the total number of puppies with spots
    total_spots = jennifer_puppies + brandon_puppies

    # Calculate the percentage of puppies with spots
    percentage_spots = (total_spots / total_puppies) * 100
    result = percentage_spots
    return result

print(solution())