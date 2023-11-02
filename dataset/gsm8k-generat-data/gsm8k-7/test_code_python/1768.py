def solution():
    current_cats = 20  # starting with 20 cats
    new_kittens = 2
    injured_cat = 1
    adopted_cats = 6  # 3 people adopting 2 cats each

    # Add new cats, subtract adopted cats and injured cat
    total_cats = current_cats + new_kittens - adopted_cats - injured_cat
    result = total_cats
    return result

print(solution())