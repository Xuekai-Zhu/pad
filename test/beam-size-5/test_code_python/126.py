def solution():
    total_workers = 60  # Nissa hires 60 seasonal workers to play elves
    elves_quit_before_vomit = total_workers / 3  # A third of the elves quit after children vomit
    elves_remaining = total_workers - elves_quit_before_vomit  # Calculate the number of remaining elves
    elves_quit_after_kids = 10  # 10 of the remaining elves quit after kids kick their shins
    elves_left = elves_remaining - elves_quit_after_kids  # Calculate the number of elves left
    result = elves_left
    return result

print(solution())