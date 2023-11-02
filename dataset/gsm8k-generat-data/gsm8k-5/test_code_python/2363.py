def solution():
    num_centipedes = 100  # Given

    # Let's assume the number of humans on the island is 'x'
    num_humans = x
    
    # Then the number of centipedes will be twice the number of humans
    num_centipedes = 2 * num_humans
    
    # And the number of sheep will be half the number of humans
    num_sheep = num_humans / 2
    
    # Total number of animals on the island will be the sum of all three
    total_animals = num_humans + num_centipedes + num_sheep
    
    # We know that the number of centipedes is 100
    # So we can solve for 'x'
    x = num_centipedes / 2
    num_humans = x
    
    # Now we can calculate the total number of animals on the island
    total_animals = num_humans + num_centipedes + num_sheep
    result = (num_humans, num_sheep)
    return result

print(solution())