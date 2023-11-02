def solution():
    """Simon collected treasures on the beach during his summer vacation. He collected a bucket of pearly seashells, a jar full of smooth sea glass, and a bag of ten sand dollars. If the jar holds three times as many pieces of glass as the bag does sand dollars, and the bucket holds five times as many seashells as the jar holds pieces of glass, how many treasures did Simon find on the beach?"""
    sand_dollars = 10
    pieces_of_glass = sand_dollars * 3
    seashells = pieces_of_glass * 5

    total_treasures = sand_dollars + pieces_of_glass + seashells
    result = total_treasures
    return result

print(solution())