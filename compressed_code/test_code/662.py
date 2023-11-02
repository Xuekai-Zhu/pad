def solution():
    
    brother_picked = 3 * 15
    kimberly_picked = 8 * brother_picked
    parents_picked = kimberly_picked - 93
    total_picked = brother_picked + kimberly_picked + parents_picked
    strawberries_per_person = total_picked / 4
    result = strawberries_per_person
    return result

print(solution())