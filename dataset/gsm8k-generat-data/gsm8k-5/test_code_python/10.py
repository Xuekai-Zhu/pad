def solution():
    # Total number of people eaten by the monster in 300 years
    total_people_eaten = 847

    # Number of people eaten in the third century
    people_eaten_third_century = total_people_eaten // 4

    # Number of people eaten in the second century
    people_eaten_second_century = people_eaten_third_century // 2

    # Number of people eaten in the first century
    people_eaten_first_century = people_eaten_second_century // 2

    result = people_eaten_first_century
    return result

print(solution())