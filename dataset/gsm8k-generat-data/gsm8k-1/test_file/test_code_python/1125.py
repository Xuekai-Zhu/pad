def solution():
    """Arnold, Madeline, Camden, and Sarah painted 56 easter eggs. Arnold and Madeline painted the same number of eggs. Camden and Sarah painted a total of 30 eggs, but Camden painted 12 more than Sarah. How many more eggs did Camden paint than Arnold?"""
    total_eggs = 56
    eggs_cands = total_eggs // 2
    eggs_cs = 30 / 2 + 6
    eggs_cm = eggs_cs + 12
    eggs_a = eggs_cands
    eggs_c = eggs_cm - eggs_cs
    diff = eggs_c - eggs_a
    result = diff
    return result

print(solution())