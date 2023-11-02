def solution():
    influential_music_genres = ["blues"]
    depeche_mode_influences = ["The Cure", "Ultravox"]
    # Check if blues is one of the influential genres for Depeche Mode
    if set(influential_music_genres).issubset(set(depeche_mode_influences)):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())