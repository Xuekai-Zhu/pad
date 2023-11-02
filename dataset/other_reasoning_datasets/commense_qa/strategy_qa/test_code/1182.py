def solution():
    warcraft_races = ["humans", "night elves", "dwarves"]
    magic_race = "dwarf"
    if magic_race in warcraft_races:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())