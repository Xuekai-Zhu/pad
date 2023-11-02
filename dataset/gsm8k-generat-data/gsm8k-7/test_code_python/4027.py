def solution():
    num_graham_crackers = 14
    num_oreos = 15
    grah_crackers_per_cheesecake = 2
    oreos_per_cheesecake = 3

    # Calculate the maximum number of cheesecakes Lionel can make
    max_num_cheesecakes = min(num_graham_crackers // grah_crackers_per_cheesecake, num_oreos // oreos_per_cheesecake)

    # Calculate the number of Graham crackers left over after making the maximum number of cheesecakes
    num_graham_crackers_leftover = num_graham_crackers - (max_num_cheesecakes * grah_crackers_per_cheesecake)

    result = num_graham_crackers_leftover
    return result

print(solution())