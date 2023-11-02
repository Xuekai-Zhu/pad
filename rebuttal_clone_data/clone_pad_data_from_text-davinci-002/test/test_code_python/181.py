def solution():
    total_cakes = 2
    total_slices = total_cakes * 8
    given_away_to_friends = total_slices / 4
    given_away_to_family = (total_slices - given_away_to_friends) / 3
    slices_eaten = 3
    total_given_away = given_away_to_friends + given_away_to_family
    slices_left = total_slices - total_given_away - slices_eaten
    result = slices_left

    return result

print(solution())