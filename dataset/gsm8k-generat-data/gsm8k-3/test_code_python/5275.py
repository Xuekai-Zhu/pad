def solution():
    """Bert, Ernie, and Peggy collect stamps.  Bert has four times as many stamps as Ernie, but Ernie has three times as many stamps as Peggy.  If Peggy currently has 75 stamps in her collection, how many stamps does she need to add to her collection to have a collection as large as Bert's collection?"""
    # Define Peggy's initial number of stamps
    peggy_stamps = 75

    # Calculate Ernie's number of stamps
    ernie_stamps = 3 * peggy_stamps

    # Calculate Bert's number of stamps
    bert_stamps = 4 * ernie_stamps

    # Calculate the number of stamps Peggy needs to add to her collection
    additional_stamps = bert_stamps - peggy_stamps

    # Display the number of stamps Peggy needs to add to her collection
    result = additional_stamps
    return result

print(solution())