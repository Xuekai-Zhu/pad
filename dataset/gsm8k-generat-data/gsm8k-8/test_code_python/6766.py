def solution():
    # Calculate the number of albums Bridget has
    bridget_albums = 30 - 15

    # Calculate the number of albums Katrina has
    katrina_albums = 6 * bridget_albums

    # Calculate the number of albums Miriam has
    miriam_albums = 5 * katrina_albums

    # Calculate the total number of albums
    total_albums = adele_albums + miriam_albums + katrina_albums + bridget_albums

    result = total_albums
    return result

print(solution())