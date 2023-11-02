def solution():
    caps_per_month_first_year = 3
    caps_per_month_after_first_year = 5
    caps_from_friends_and_family_per_year = 40
    caps_lost_per_year = 15
    years_collected = 5

    # Calculate the total number of caps collected in the first year
    caps_first_year = caps_per_month_first_year * 12

    # Calculate the total number of caps collected after the first year
    caps_after_first_year = (caps_per_month_after_first_year * 12) * (years_collected - 1)

    # Calculate the total number of caps received from friends and family
    caps_from_friends_and_family = caps_from_friends_and_family_per_year * years_collected

    # Calculate the total number of caps lost
    caps_lost = caps_lost_per_year * years_collected

    # Calculate the total number of caps collected
    total_caps_collected = caps_first_year + caps_after_first_year + caps_from_friends_and_family - caps_lost
    result = total_caps_collected
    return result

print(solution())