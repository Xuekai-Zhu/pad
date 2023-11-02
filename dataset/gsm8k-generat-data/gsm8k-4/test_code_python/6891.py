def solution():
    """Ben took his family fishing yesterday. Ben caught 4 fish, his wife Judy caught 1 fish, his oldest son Billy caught 3, his younger son Jim caught 2, and his youngest child Susie surprised them all by catching 5! Unfortunately, 3 of the fish were too small, so they threw them back. If each fish will give them 2 filets, how many fish filets will Ben and his family have?"""
    # Define the number of fish caught by each family member
    ben_fish = 4
    judy_fish = 1
    billy_fish = 3
    jim_fish = 2
    susie_fish = 5

    # Add up the total number of fish caught
    total_fish = ben_fish + judy_fish + billy_fish + jim_fish + susie_fish

    # Subtract the number of small fish
    total_fish -= 3

    # Calculate the total number of filets
    total_filets = total_fish * 2

    result = total_filets
    return result

print(solution())