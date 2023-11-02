def solution():
    """Remi prepared a tomato nursery and planted tomato seedlings. After 20 days, the seedlings were ready to be transferred. On the first day, he planted 200 seedlings on the farm. On the second day, while working alongside his father, he planted twice the number of seedlings he planted on the first day. If the total number of seedlings transferred to the farm on these two days was 1200, how many seedlings did his father plant?"""
    # Define the number of seedlings planted on the first day
    day_one_seedlings = 200

    # Calculate the number of seedlings planted by Remi on the second day
    day_two_seedlings = 2 * day_one_seedlings

    # Calculate the total number of seedlings planted by Remi and his father
    total_seedlings = day_one_seedlings + day_two_seedlings

    # Calculate the number of seedlings planted by Remi's father
    father_seedlings = 1200 - total_seedlings

    # Return the result
    result = father_seedlings
    return result

print(solution())