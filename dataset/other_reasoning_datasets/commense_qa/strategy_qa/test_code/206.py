def solution():
    days_of_our_lives_episodes = 13900
    general_hospital_episodes = 14000
    dollar_amount = 1000
    if days_of_our_lives_episodes * dollar_amount < general_hospital_episodes * dollar_amount:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())