def solution():
    """Tricia is a third of Amilia’s age and Amilia is a quarter of Yorick’s age. Yorick is twice Eugene’s age and Khloe is a third of Eugene’s age. Rupert is 10 years older than Khloe but 2 years younger than Vincent who is 22 years old. How old, in years, is Tricia?"""
    vincent_age = 22
    rupert_age = vincent_age - 2
    eugene_age = vincent_age / 2 / 3
    khloe_age = eugene_age / 3
    yorick_age = eugene_age * 2
    amilia_age = yorick_age / 4
    tricia_age = amilia_age / 3
    result = tricia_age
    return result

print(solution())