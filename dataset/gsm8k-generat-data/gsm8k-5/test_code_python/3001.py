def solution():
    total_ladies = 5  # Jamie is in a walking group with 4 other ladies
    group_distance = 3  # The ladies all walk 3 miles together
    jamie_extra_distance = 2  # Jamie walks an additional 2 miles per day for 6 days
    sue_extra_distance = jamie_extra_distance / 2  # Sue walks half of Jamie's extra distance
    extra_days = 6  # They walk this same route 6 days a week

    # Calculate the total distance Jamie walks in a week
    jamie_total_distance = group_distance + (jamie_extra_distance * extra_days)

    # Calculate the total distance Sue walks in a week
    sue_total_distance = group_distance + (sue_extra_distance * extra_days)

    # Calculate the total distance all ladies walk in a week
    total_distance = (jamie_total_distance + sue_total_distance) * total_ladies

    result = total_distance
    return result

print(solution())