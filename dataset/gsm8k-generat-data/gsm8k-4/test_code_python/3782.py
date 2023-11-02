def solution():
    """Simon collected treasures on the beach during his summer vacation. He collected a bucket of pearly seashells, a jar full of smooth sea glass, and a bag of ten sand dollars. If the jar holds three times as many pieces of glass as the bag does sand dollars, and the bucket holds five times as many seashells as the jar holds pieces of glass, how many treasures did Simon find on the beach?"""
    # Define the initial number of sand dollars
    sand_dollars = 10

    # Calculate the number of pieces of glass in the jar
    jar_glass = sand_dollars * 3

    # Calculate the number of seashells in the bucket
    bucket_seashells = jar_glass * 5

    # Calculate the total number of treasures
    total_treasures = sand_dollars + jar_glass + bucket_seashells

    # return the result
    result = total_treasures
    return result

print(solution())