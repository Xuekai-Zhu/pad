def solution():
    # Find the number of fish that Angus caught
    angus_fish = 5 + 7  # Ollie caught 7 fewer fish than Angus, so Angus caught (5 + 7) fish
    # Find the number of fish that Patrick caught
    patrick_fish = angus_fish - 4  # Angus caught 4 more fish than Patrick, so Patrick caught (Angus's fish - 4) fish
    result = patrick_fish
    return result

print(solution())