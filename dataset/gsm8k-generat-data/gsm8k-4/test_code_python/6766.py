def solution():
    """Miriam has five times as many albums as Katrina. Katrina has six times the number of albums as Bridget. Bridget has 15 fewer albums than Adele. How many albums do they have together if Adele has 30 albums?"""
    # Define the number of albums Adele has
    adele_albums = 30

    # Calculate the number of albums Bridget has
    bridget_albums = adele_albums - 15

    # Calculate the number of albums Katrina has
    katrina_albums = bridget_albums * 6

    # Calculate the number of albums Miriam has
    miriam_albums = katrina_albums * 5

    # Calculate the total number of albums they have together
    total_albums = adele_albums + bridget_albums + katrina_albums + miriam_albums

    # return the result
    result = total_albums
    return result

print(solution())