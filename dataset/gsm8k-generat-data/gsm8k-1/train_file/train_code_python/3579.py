def solution():
    """Remi prepared a tomato nursery and planted tomato seedlings. After 20 days, the seedlings were ready to be transferred. On the first day, he planted 200 seedlings on the farm. On the second day, while working alongside his father, he planted twice the number of seedlings he planted on the first day. If the total number of seedlings transferred to the farm on these two days was 1200, how many seedlings did his father plant?"""
    day_one = 200
    day_two = day_one * 2
    total = day_one + day_two
    father_planted = 1200 - total
    result = father_planted
    return result

print(solution())