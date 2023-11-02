def solution():
    # Calculate the number of pairs of students
    num_pairs = 20 / 2

    # Calculate the number of students making 3 artworks each
    num_3_artists = 10 / 2

    # Calculate the number of students making 4 artworks each
    num_4_artists = 10 / 2

    # Calculate the total number of artworks created
    total_num_artworks = (num_3_artists * 3) + (num_4_artists * 4)

    result = total_num_artworks
    return result

print(solution())