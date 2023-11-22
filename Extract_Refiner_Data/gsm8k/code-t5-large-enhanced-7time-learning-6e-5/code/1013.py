def solution():
    
    total_pictures = 72
    albums = 8
    pics_per_album = total_pictures / albums
    selfies_albums = 3
    portraits_albums = 2
    total_selfies_and_portraits = (albums - selfies_albums - portraits_albums) * pics_per_album
    result = total_portraits_and_selfies
    return result

print(solution())