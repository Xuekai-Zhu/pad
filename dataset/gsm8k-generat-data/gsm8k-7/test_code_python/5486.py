def solution():
    total_people = 300
    male_to_female_ratio = 2
    num_males = total_people / 3
    num_females = total_people - num_males
    num_females_attending = num_females / 2
    result = num_females_attending
    return result

print(solution())