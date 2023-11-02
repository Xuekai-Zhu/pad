def solution():
    total_contestants = 18  # There are 18 contestants in total
    female_contestants = total_contestants / 3  # One third of the contestants are female
    male_contestants = total_contestants - female_contestants  # The rest of the contestants are male
    result = male_contestants
    return result

print(solution())