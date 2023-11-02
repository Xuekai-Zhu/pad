def solution():
    """Simon collected treasures on the beach during his summer vacation. He collected a bucket of pearly seashells, a jar full of smooth sea glass, and a bag of ten sand dollars. If the jar holds three times as many pieces of glass as the bag does sand dollars, and the bucket holds five times as many seashells as the jar holds pieces of glass, how many treasures did Simon find on the beach?"""
    # Define the number of sand dollars
    sand_dollars = 10

    # Calculate the number of pieces of sea glass in the jar
    sea_glass = 3 * sand_dollars

    # Calculate the number of seashells in the bucket
    seashells = 5 * sea_glass

    # Calculate the total number of treasures collected
    total_treasures = sand_dollars + sea_glass + seashells

    # Display the total number of treasures
    result = total_treasures
    return result

print(solution())