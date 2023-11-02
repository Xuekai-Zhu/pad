def solution():
    """Miriam has five times as many albums as Katrina. Katrina has six times the number of albums as Bridget. Bridget has 15 fewer albums than Adele. How many albums do they have together if Adele has 30 albums?"""
    adele_albums = 30
    bridget_albums = adele_albums - 15
    katrina_albums = 6 * bridget_albums
    miriam_albums = 5 * katrina_albums
    total_albums = adele_albums + bridget_albums + katrina_albums + miriam_albums
    result = total_albums
    return result

print(solution())