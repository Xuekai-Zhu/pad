def solution():
    """Naomi is doing the wash. First she makes piles of different types, with one pile for towels, one for sheets, and one for clothes that need to be washed on the gentle cycle. The clothes take 30 minutes to wash. The towels take twice as long as the clothes to wash. The sheets take 15 minutes less time to wash than the towels. How many minutes total will it take for Naomi to wash everything?"""
    clothes_wash_time = 30
    towels_wash_time = clothes_wash_time * 2
    sheets_wash_time = towels_wash_time - 15
    total_wash_time = clothes_wash_time + towels_wash_time + sheets_wash_time
    result = total_wash_time
    return result

print(solution())