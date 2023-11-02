def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_last_name = "Grey"
    bobbie_last_name = jamie_last_name + "XXXX"
    samantha_last_name = bobbie_last_name[:-3]
    bobbie_last_name = bobbie_last_name[:-2]
    if len(bobbie_last_name) == len(jamie_last_name)*2:
        result = len(samantha_last_name)
    else:
        result = "Cannot determine Samantha's last name length"
    return result


def solution():
    """Britany records 18 4-minute TikTok videos each week. She spends 2 hours a week writing amateur songs to sing on TikTok, and 15 minutes six days a week doing her makeup before filming herself for TikTok. How much time does Britany spend on TikTok in a month with four weeks?"""
    tiktok_videos_per_week = 18
    minutes_spent_on_makeup_per_day = 15
    hours_spent_on_songs_per_week = 2
    minutes_spent_on_makeup_per_week = minutes_spent_on_makeup_per_day * 6
    total_time_spent_on_tiktok_per_week = tiktok_videos_per_week * 4 + (hours_spent_on_songs_per_week * 60) + minutes_spent_on_makeup_per_week
    total_time_spent_on_tiktok_in_month = total_time_spent_on_tiktok_per_week * 4
    result = total_time_spent_on_tiktok_in_month
    return result

print(solution())