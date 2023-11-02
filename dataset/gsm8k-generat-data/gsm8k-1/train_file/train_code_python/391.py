def solution():
    """Naomi is doing the wash. First she makes piles of different types, with one pile for towels, one for sheets, and one for clothes that need to be washed on the gentle cycle. The clothes take 30 minutes to wash. The towels take twice as long as the clothes to wash. The sheets take 15 minutes less time to wash than the towels. How many minutes total will it take for Naomi to wash everything?"""
    clothes = 30
    towels = clothes * 2
    sheets = towels - 15
    total_time = clothes + towels + sheets
    result = total_time
    return result

print(solution())