def solution():
    """Paul goes fishing every Saturday. Last week he was able to catch 5 fish for every 2 hours he was fishing. How many fish did he catch when he was fishing for 12 hours?"""
    fish_per_two_hours = 5
    total_hours = 12
    total_fish = (fish_per_two_hours / 2) * total_hours
    result = total_fish
    return result

print(solution())