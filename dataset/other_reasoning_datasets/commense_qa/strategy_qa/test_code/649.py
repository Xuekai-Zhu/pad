def solution():
    metallica_oppose_digital_piracy = True
    soulseek_is_used_for_illegal_music_sharing = True
    if metallica_oppose_digital_piracy and not soulseek_is_used_for_illegal_music_sharing:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())