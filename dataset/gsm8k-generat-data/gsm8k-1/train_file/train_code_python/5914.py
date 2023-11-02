def solution():
    """Michael bought 6 crates of egg on Tuesday. He gave out 2 crates to Susan, who he admires and bought another 5 crates on Thursday. If one crate holds 30 eggs, how many eggs does he have now?"""
    crates_on_tuesday = 6
    crates_given = 2
    crates_on_thursday = 5
    eggs_per_crate = 30
    total_eggs = (crates_on_tuesday - crates_given + crates_on_thursday) * eggs_per_crate
    result = total_eggs
    return result

print(solution())