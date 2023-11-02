def solution():
    """Porter is a painter who creates beautiful paintings of wild animals.  Most recently, he painted a mural of a pack of wolves standing on a snowy-white mountainside underneath a full moon.  He put the painting up for auction and it sold for $1000 less than five times more than he had made on his previous painting.  If he received $44,000 for the sale of his most recent painting, how much, in dollars, did he make for selling his previous painting?"""
    # Define the amount by which the most recent painting sold for as a multiple of the previous painting
    MULTIPLE = 5

    # Define the amount by which the most recent painting sold for less than the multiple times of the previous painting
    LESS = 1000

    # Calculate the amount made from the most recent painting
    recent_painting = 44000

    # Calculate the amount made from the previous painting
    previous_painting = (recent_painting + LESS) / (MULTIPLE * 1.0)

    # Display the amount made from the previous painting
    result = previous_painting
    return result

print(solution())