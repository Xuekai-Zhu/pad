def solution():
    total_members = 18
    ratio_female_male = 2  # two times as many female than male

    # Calculate the total number of males in the club
    num_males = total_members / (ratio_female_male + 1)

    # Calculate the total number of females in the club
    num_females = num_males * ratio_female_male
    result = num_females
    return result

print(solution())