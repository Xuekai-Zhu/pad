def solution():
    
    total_fishermen = 20
    total_fish_caught = 10000
    fish_caught_per_person = 400
    fish_caught_by_nineteen = 19 * fish_caught_per_person
    fish_caught_by_twentieth = total_fish_caught - fish_caught_by_nineteen
    result = fish_caught_by_twentieth
    return result

print(solution())