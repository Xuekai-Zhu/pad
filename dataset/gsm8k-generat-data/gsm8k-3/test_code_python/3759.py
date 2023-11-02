def solution():
    """A van is delivering  180 bottles of drinks to a neighborhood, and each bottle contains either cider or beer or a mixture of two. Out of the  180 bottles, 40 contain only cider, 80 contain only beer, and the rest are a mixture of the two drinks. If the delivery man gives half the number of each bottle of drink to the first house, how many bottles does the first house get?"""
    
    # Define the number of bottles containing only cider and beer
    cider_only = 40
    beer_only = 80

    # Calculate the number of bottles containing a mixture of cider and beer
    mixture = 180 - cider_only - beer_only

    # Calculate the total number of bottles to be split between the houses
    total = (cider_only + beer_only + mixture) / 2

    # Calculate the number of bottles of each type to be given to the first house
    first_house = (cider_only + beer_only + mixture) / 4

    # Display the number of bottles the first house gets
    result = first_house
    return result

print(solution())