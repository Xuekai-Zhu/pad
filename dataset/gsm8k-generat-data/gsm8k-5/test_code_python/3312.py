def solution():
    num_minor_characters = 4
    num_major_characters = 5
    minor_character_salary = 15000
    major_character_salary = minor_character_salary * 3

    total_minor_character_salary = num_minor_characters * minor_character_salary
    total_major_character_salary = num_major_characters * major_character_salary

    total_salary_per_episode = total_minor_character_salary + total_major_character_salary
    result = total_salary_per_episode
    return result

print(solution())