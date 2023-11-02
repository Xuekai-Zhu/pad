def solution():
    # Calculate the amount of water a single barrel can store
    cask = 20  # gallons in a cask
    barrel = 2*cask + 3  # barrels store 3 gallons more than twice the amount a cask can store

    # Calculate the total amount of water James can store
    total_water = barrel * 4 + cask
    result = total_water
    return result

print(solution())