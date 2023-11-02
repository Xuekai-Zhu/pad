def solution():
    """Stan can type 50 words per minute. He needs to write a 5-page paper. Each page will contain 400 words. Each hour that he types he needs to drink 15 ounces of water. How much water does he need to drink while writing his paper?"""
    words_per_page = 400
    total_words = words_per_page * 5
    typing_speed = 50
    typing_time = total_words / typing_speed
    water_per_hour = 15
    water_needed = (typing_time / 60) * water_per_hour
    result = water_needed
    return result

print(solution())