def solution():
    # Define the number of heads and legs for one emu
    emu_heads = 1
    emu_legs = 2

    # Define the total number of heads and legs for the whole flock
    total_heads = 60
    total_legs = total_heads * 2

    # Calculate the number of emus in the flock
    num_emus = (total_legs - total_heads) / (emu_legs - emu_heads)
    result = num_emus
    return result

print(solution())