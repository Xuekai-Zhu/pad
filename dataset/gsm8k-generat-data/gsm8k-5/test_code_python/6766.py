def solution():
    adele_albums = 30  # Adele has 30 albums
    bridget_albums = adele_albums - 15  # Bridget has 15 fewer albums than Adele
    katrina_albums = 6 * bridget_albums  # Katrina has six times the number of albums as Bridget
    miriam_albums = 5 * katrina_albums  # Miriam has five times as many albums as Katrina

    # Calculate the total number of albums they have together
    total_albums = adele_albums + bridget_albums + katrina_albums + miriam_albums
    result = total_albums
    return result

print(solution())