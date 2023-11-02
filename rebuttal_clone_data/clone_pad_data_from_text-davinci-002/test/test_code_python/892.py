def solution():
    notebooks = 4
    notebook_stamps = 20
    binders = 2
    binder_stamps = 50
    stamps_to_keep = (notebooks * notebook_stamps + binders * binder_stamps) / 4
    stamps_to_give_away = notebooks * notebook_stamps + binders * binder_stamps - stamps_to_keep
    result = stamps_to_give_away
    return result

print(solution())