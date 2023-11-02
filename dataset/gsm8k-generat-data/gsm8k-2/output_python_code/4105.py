def solution():
    """Solomon collected three times as many cans as Juwan. Levi collected half of what Juwan collected. Solomon collected 66 cans. How many cans did the boys collect in all?"""
    solomon_cans = 66
    juwan_cans = solomon_cans / 3
    levi_cans = juwan_cans / 2
    total_cans = solomon_cans + juwan_cans + levi_cans
    result = total_cans
    return result

print(solution())