def solution():
    channels = 150
    channels_removed = 20
    channels_added = 12
    channels_reduced = 10
    channels_sports = 8
    channels_supreme_sports = 7
    channels_final = channels + channels_added - channels_removed - channels_reduced + channels_sports + channels_supreme_sports
    result = channels_final
    return result

print(solution())