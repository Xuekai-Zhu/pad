def solution():
    julian_friends = 80  # Julian has 80 Facebook friends
    julian_girls = julian_friends * 0.4  # 40% of Julian's friends are girls
    boyd_friends = 100  # Boyd has 100 Facebook friends
    boyd_girls = (julian_girls * 2)  # Boyd has twice as many friends who are girls as Julian
    boyd_boys = boyd_friends - boyd_girls  # Calculate how many of Boyd's friends are boys

    # Calculate the percentage of Boyd's friends who are boys
    percentage_boys = (boyd_boys / boyd_friends) * 100
    result = percentage_boys
    return result

print(solution())