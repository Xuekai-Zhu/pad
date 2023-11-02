def solution():
    # Calculate the total number of water balloons available
    total_balloons = (3 + 2) * 6  # Milly and Floretta use 3 packs of their own balloons and 2 packs of the neighbor's balloons, each pack contains 6 balloons

    # Calculate the number of balloons Floretta has after Milly takes 7 extra
    floretta_balloons = total_balloons // 2 - 7  # split evenly and subtract 7 extra taken by Milly
    result = floretta_balloons
    return result

print(solution())