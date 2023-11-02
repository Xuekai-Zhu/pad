def solution():
    caps_per_month_first_year = 3
    caps_per_month_after_first_year = 5
    caps_received_at_christmas = 40
    caps_lost_per_year = 15
    num_years = 5

    # Calculate the total number of caps collected in the first year
    total_caps_first_year = caps_per_month_first_year * 12

    # Calculate the total number of caps collected in the following years
    total_caps_following_years = (caps_per_month_after_first_year * 12) * (num_years - 1)

    # Calculate the total number of caps received at Christmas
    total_caps_at_christmas = caps_received_at_christmas * num_years

    # Calculate the total number of caps lost over the years
    total_caps_lost = caps_lost_per_year * num_years

    # Calculate the total number of caps collected so far
    total_caps = total_caps_first_year + total_caps_following_years + total_caps_at_christmas - total_caps_lost
    result = total_caps
    return result

print(solution())