def solution():
    minutes_per_day = 180
    minutes_per_segment = 10
    minutes_per_ad = 5
    talking_segments = 3
    ad_breaks = 5
    minutes_talking = minutes_per_segment * talking_segments
    minutes_ads = minutes_per_ad * ad_breaks
    minutes_playing_songs = minutes_per_day - minutes_talking - minutes_ads
    result = minutes_playing_songs
    return result

print(solution())