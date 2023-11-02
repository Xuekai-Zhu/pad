def solution():
    julian_friends = 80
    julian_boy_friends = 80 * (60 / 100)
    julian_girl_friends = 80 * (40 / 100)
    boyd_friends = 100
    boyd_girl_friends = 2 * julian_girl_friends
    boyd_boy_friends = boyd_friends - boyd_girl_friends
    boyd_boy_friend_percentage = boyd_boy_friends / boyd_friends * 100
    result = boyd_boy_friend_percentage
    return result

print(solution())