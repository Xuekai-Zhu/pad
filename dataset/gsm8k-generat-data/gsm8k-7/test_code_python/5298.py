def solution():
    starting_cans = 2000
    day_one_people = 500
    day_one_cans_per_person = 1
    day_one_taken = day_one_people * day_one_cans_per_person

    restock_one = 1500

    day_two_people = 1000
    day_two_cans_per_person = 2
    day_two_taken = day_two_people * day_two_cans_per_person

    restock_two = 3000

    total_given_away = day_one_taken + day_two_taken
    result = total_given_away
    return result

print(solution())