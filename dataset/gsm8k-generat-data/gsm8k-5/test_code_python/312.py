def solution():
    total_heads_and_legs = 60  # The flock has a total of 60 heads and legs
    emu_legs = 2  # Emus have 2 legs
    emu_heads = 1  # Emus have 1 head

    # Use a system of equations to solve for the number of emus in the flock
    # Let x be the number of emus in the flock
    # Then 2x represents the total number of legs and x represents the total number of heads
    # The total number of heads and legs is also given as 60
    # So we can write: 2x + x = 60, which simplifies to 3x = 60 and x = 20

    number_of_emus = 20
    result = number_of_emus
    return result

print(solution())