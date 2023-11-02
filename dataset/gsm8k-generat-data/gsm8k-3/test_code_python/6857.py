def solution():
    """Archer caught eight fish from the lake to sell in the market. When he reached the market, he sold the fish faster than he had anticipated and decided to go back to the lake and catch more fish. He caught 12 more fish in the second round than he had caught earlier. The demand was even greater, and he had to close the day by catching 60% more fish than the number he had caught in the second round and sold all of them in the market. How many fish did he catch that day?"""
    # Define the number of fish caught in the first round
    fish_first_round = 8

    # Calculate the number of fish caught in the second round
    fish_second_round = fish_first_round + 12

    # Calculate the number of fish caught in the third round
    fish_third_round = fish_second_round * 1.6

    # Calculate the total number of fish caught that day
    total_fish = fish_first_round + fish_second_round + fish_third_round

    # Display the total number of fish
    result = total_fish
    return result

print(solution())