def solution():
    # Calculate number of albums for all four people
    num_albums_adele = 30
    num_albums_bridget = num_albums_adele - 15
    num_albums_katrina = 6 * num_albums_bridget
    num_albums_miriam = 5 * num_albums_katrina

    # Calculate total number of albums
    total_albums = num_albums_adele + num_albums_bridget + num_albums_katrina + num_albums_miriam
    result = total_albums
    return result

print(solution())