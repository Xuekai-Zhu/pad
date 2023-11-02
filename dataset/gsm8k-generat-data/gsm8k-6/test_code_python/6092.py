def solution():
    # Calculate the total number of toilet paper rolls needed for 4 weeks
    rolls_needed = 6 * 7 * 4  # 6 bathrooms, 7 days a week, for 4 weeks
    # Calculate the total number of packs of toilet paper dozens needed
    packs_needed = rolls_needed // 12 + 1  # Each pack contains 1 dozen rolls; add 1 to round up to the nearest pack
    result = packs_needed
    return result

print(solution())