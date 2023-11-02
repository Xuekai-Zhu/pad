def solution():
    times_hunted_per_month = 6
    months_in_quarter = 3
    hunts_per_quarter = times_hunted_per_month * months_in_quarter
    deer_caught_per_hunt = 2
    deer_weight_per_animal = 600
    total_deer_weight_caught = deer_caught_per_hunt * hunts_per_quarter * deer_weight_per_animal
    deer_weight_kept = total_deer_weight_caught / 2
    result = deer_weight_kept
    
    return result

print(solution())