def solution():
    jukebox_musicals = ["Mamma Mia!", "Jersey Boys", "Rock of Ages"]
    rocky_horror_contains_original_songs = True
    rocky_horror_about_transvestite = True
    expected_title = "The Rocky Horror Picture Show"
    if expected_title not in jukebox_musicals and rocky_horror_contains_original_songs and rocky_horror_about_transvestite:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())