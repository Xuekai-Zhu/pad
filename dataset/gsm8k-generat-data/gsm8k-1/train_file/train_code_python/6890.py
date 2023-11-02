def solution():
    """Ben took his family fishing yesterday. Ben caught 4 fish, his wife Judy caught 1 fish, his oldest son Billy caught 3, his younger son Jim caught 2, and his youngest child Susie surprised them all by catching 5! Unfortunately, 3 of the fish were too small, so they threw them back. If each fish will give them 2 filets, how many fish filets will Ben and his family have?"""
    ben = 4
    judy = 1
    billy = 3
    jim = 2
    susie = 5
    total_fish = ben + judy + billy + jim + susie
    usable_fish = total_fish - 3
    filets_per_fish = 2
    total_filets = usable_fish * filets_per_fish
    result = total_filets
    return result

print(solution())