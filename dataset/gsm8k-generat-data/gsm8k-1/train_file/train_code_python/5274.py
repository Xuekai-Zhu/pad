def solution():
    """Bert, Ernie, and Peggy collect stamps. Bert has four times as many stamps as Ernie, but Ernie has three times as many stamps as Peggy. If Peggy currently has 75 stamps in her collection, how many stamps does she need to add to her collection to have a collection as large as Bert's collection?"""
    peggy_stamps = 75
    ernie_stamps = peggy_stamps * 3
    bert_stamps = ernie_stamps * 4
    stamps_to_add = bert_stamps - peggy_stamps
    result = stamps_to_add
    return result

print(solution())