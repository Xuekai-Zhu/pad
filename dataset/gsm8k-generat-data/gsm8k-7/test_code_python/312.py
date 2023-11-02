def solution():
    num_heads_and_legs = 60
    emu_legs = 2  # Each emu has two legs

    # Assume all animals in the flock are emus
    num_emus = num_heads_and_legs // emu_legs

    result = num_emus
    return result

print(solution())