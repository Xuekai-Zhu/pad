def solution():
    sand_dollars = 10  # Simon collected 10 sand dollars in a bag
    glass_pieces = sand_dollars * 3  # The jar holds 3 times as many pieces of glass as the bag holds sand dollars
    seashells = glass_pieces * 5  # The bucket holds 5 times as many seashells as the jar holds glass pieces

    # Calculate the total number of treasures Simon found on the beach
    total_treasures = sand_dollars + glass_pieces + seashells
    result = total_treasures
    return result

print(solution())