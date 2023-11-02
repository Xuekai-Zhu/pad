def solution():
    """Marie has 4 notebooks with 20 stamps each. She also has two binders with 50 stamps each. If she decides to only keep 1/4 of the stamps, how many stamps can she give away?"""
    notebooks = 4
    binder = 2
    stamps_per_notebook = 20
    stamps_per_binder = 50
    total_stamps = (notebooks * stamps_per_notebook) + (binder * stamps_per_binder)
    stamps_to_keep = total_stamps / 4
    stamps_to_give_away = total_stamps - stamps_to_keep
    result = stamps_to_give_away
    return result

print(solution())