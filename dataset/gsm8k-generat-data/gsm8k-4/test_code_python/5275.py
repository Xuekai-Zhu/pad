def solution():
    """Bert, Ernie, and Peggy collect stamps. Bert has four times as many stamps as Ernie, but Ernie has three times as many stamps as Peggy. If Peggy currently has 75 stamps in her collection, how many stamps does she need to add to her collection to have a collection as large as Bert's collection?"""
    # Calculate the number of stamps Ernie has
    ernie_stamps = 75 * 3

    # Calculate the number of stamps Bert has
    bert_stamps = ernie_stamps * 4

    # Calculate the number of stamps Peggy needs to add to her collection to have as many stamps as Bert
    peggy_stamps_needed = bert_stamps - 75

    result = peggy_stamps_needed
    return result

print(solution())