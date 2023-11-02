def solution():
    """Archer caught eight fish from the lake to sell in the market. When he reached the market, he sold the fish faster than he had anticipated and decided to go back to the lake and catch more fish. He caught 12 more fish in the second round than he had caught earlier. The demand was even greater, and he had to close the day by catching 60% more fish than the number he had caught in the second round and sold all of them in the market. How many fish did he catch that day?"""
    first_round = 8
    second_round = first_round + 12
    third_round = 1.6 * second_round
    total_fish = first_round + second_round + third_round
    result = total_fish
    return result

print(solution())