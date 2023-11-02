def solution():
    julian_total_friends = 80
    julian_boy_percentage = 60
    julian_girl_percentage = 40

    boyd_total_friends = 100
    boyd_girl_friends = julian_girl_percentage / 100 * julian_total_friends * 2

    boyd_boy_friends = boyd_total_friends - boyd_girl_friends

    boyd_boy_percentage = boyd_boy_friends / boyd_total_friends * 100

    result = boyd_boy_percentage

    return result

print(solution())