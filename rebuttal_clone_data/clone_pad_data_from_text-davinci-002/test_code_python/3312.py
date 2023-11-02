def solution():
    main_characters = 5
    minor_characters = 4
    pay_per_episode = 15000
    main_character_pay = pay_per_episode * 3
    total_pay_per_episode = main_character_pay + (minor_characters * pay_per_episode)
    result = total_pay_per_episode
    return result

print(solution())