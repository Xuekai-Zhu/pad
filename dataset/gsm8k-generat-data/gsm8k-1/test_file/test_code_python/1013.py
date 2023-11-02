def solution():
    """Olivia uploaded 72 pictures to Facebook. She put the same number of the pics into 8 albums. 3 of the albums were selfies only and 2 of the albums were portraits. How many portraits and selfies did she have?"""
    total_pictures = 72
    total_albums = 8
    selfies_albums = 3
    portraits_albums = 2
    pictures_per_album = total_pictures / total_albums
    selfies = selfies_albums * pictures_per_album
    portraits = portraits_albums * pictures_per_album
    result = (selfies, portraits)
    return result

print(solution())