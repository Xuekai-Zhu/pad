def solution():
    """If Aang caught 7 fish, then Sokka caught 5 fish, and then Toph caught 12 fish, what is the average amount of fish that each person caught?"""
    total_fish = 7 + 5 + 12
    num_people = 3
    avg_fish_per_person = total_fish / num_people
    result = avg_fish_per_person
    return result

print(solution())