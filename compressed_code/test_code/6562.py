def solution():
    
    total_eyes = 22
    eyes_per_fish = 2
    total_people = 3
    total_eyes_given_away = 2
    total_fish = (total_eyes + total_eyes_given_away) / eyes_per_fish
    fish_per_person = total_fish / total_people
    result = fish_per_person
    return result

print(solution())