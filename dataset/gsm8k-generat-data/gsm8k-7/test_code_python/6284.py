def solution():
    num_stories = 20
    lola_time = 10 * num_stories  # time for Lola to run up the stairs
    tara_time = 8 * num_stories + 3 * num_stories  # time for Tara to take the elevator with stops at each floor

    slower_time = max(lola_time, tara_time)  # find the slower time

    result = slower_time
    return result

print(solution())