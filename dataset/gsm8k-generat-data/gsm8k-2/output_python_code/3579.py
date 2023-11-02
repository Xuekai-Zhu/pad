def solution():
    """Remi prepared a tomato nursery and planted tomato seedlings. After 20 days, the seedlings were ready to be transferred. On the first day, he planted 200 seedlings on the farm. On the second day, while working alongside his father, he planted twice the number of seedlings he planted on the first day. If the total number of seedlings transferred to the farm on these two days was 1200, how many seedlings did his father plant?"""
    total_planted = 1200
    first_day_planted = 200
    second_day_planted = 2 * first_day_planted
    remi_planted = first_day_planted + second_day_planted
    father_planted = total_planted - remi_planted
    result = father_planted
    return result

print(solution())