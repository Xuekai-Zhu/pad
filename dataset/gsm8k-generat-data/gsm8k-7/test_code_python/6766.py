def solution():
    adele_albums = 30
    bridget_albums = adele_albums - 15
    katrina_albums = 6 * bridget_albums
    miriam_albums = 5 * katrina_albums
    total_albums = adele_albums + bridget_albums + katrina_albums + miriam_albums
    result = total_albums
    return result

print(solution())