def solution():
    
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