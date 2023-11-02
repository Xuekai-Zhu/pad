def solution():
    capacity_of_Dorton_Arena = 7610
    daily_passengers_at_30th_Street = 12000
    if daily_passengers_at_30th_Street <= capacity_of_Dorton_Arena:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())