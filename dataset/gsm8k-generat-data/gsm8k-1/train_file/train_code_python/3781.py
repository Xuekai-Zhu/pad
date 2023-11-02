def solution():
    """Simon collected treasures on the beach during his summer vacation. He collected a bucket of pearly seashells, a jar full of smooth sea glass, and a bag of ten sand dollars. If the jar holds three times as many pieces of glass as the bag does sand dollars, and the bucket holds five times as many seashells as the jar holds pieces of glass, how many treasures did Simon find on the beach?"""
    sand_dollars = 10
    glass_pieces = sand_dollars * 3
    seashells = glass_pieces * 5
    total_treasures = sand_dollars + glass_pieces + seashells
    result = total_treasures
    return result

print(solution())