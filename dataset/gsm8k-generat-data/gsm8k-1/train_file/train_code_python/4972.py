def solution():
    """James catches 3 kinds of fish. He catches 200 pounds of trout, 50% more pounds of salmon, and twice as much Tuna. How many pounds of fish did he catch?"""
    trout = 200
    salmon = trout * 1.5
    tuna = trout * 2
    total_fish = trout + salmon + tuna
    result = total_fish
    return result

print(solution())