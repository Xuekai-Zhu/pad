def solution():
    """Ben took his family fishing yesterday. Ben caught 4 fish, his wife Judy caught 1 fish, his oldest son Billy caught 3, his younger son Jim caught 2, and his youngest child Susie surprised them all by catching 5! Unfortunately, 3 of the fish were too small, so they threw them back. If each fish will give them 2 filets, how many fish filets will Ben and his family have?"""
    total_fish = 4 + 1 + 3 + 2 + 5 - 3
    total_fish_filets = total_fish * 2
    result = total_fish_filets
    return result

print(solution())