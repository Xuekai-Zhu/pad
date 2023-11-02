def solution():
    spiders = 3
    ants = 12
    ladybugs = 8
    ladybugs_fly_away = 2

    # Calculate the total number of insects
    total_insects = spiders + ants + ladybugs

    # Subtract the number of flying ladybugs to get the remaining insects
    remaining_insects = total_insects - ladybugs_fly_away
    result = remaining_insects
    return result

print(solution())