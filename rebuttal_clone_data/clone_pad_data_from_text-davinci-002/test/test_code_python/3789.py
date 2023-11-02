def solution():
    albums_adele = 30
    albums_bridget = albums_adele - 15
    albums_katrina = albums_bridget * 6
    albums_miriam = albums_katrina * 5
    total_albums = albums_adele + albums_bridget + albums_katrina + albums_miriam
    result = total_albums
    return result

print(solution())