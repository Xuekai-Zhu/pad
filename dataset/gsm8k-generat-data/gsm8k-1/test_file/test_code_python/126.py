def solution():
    """Nissa hires 60 seasonal workers to play elves in her department store's Santa village. A third of the elves quit after children vomit on them, then 10 of the remaining elves quit after kids kick their shins. How many elves are left?"""
    initial_elves = 60
    elves_after_vomit = initial_elves - (initial_elves // 3)
    elves_left = elves_after_vomit - 10
    
    return elves_left

print(solution())