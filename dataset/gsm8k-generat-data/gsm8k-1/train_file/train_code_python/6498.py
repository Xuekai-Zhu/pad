def solution():
    """Tricia is a third of Amilia’s age and Amilia is a quarter of Yorick’s age. Yorick is twice Eugene’s age and Khloe is a third of Eugene’s age. Rupert is 10 years older than Khloe but 2 years younger than Vincent who is 22 years old. How old, in years, is Tricia?"""
    # Vincent is 22 years old.
    vincent_age = 22
    
    # Rupert is 2 years younger than Vincent.
    rupert_age = vincent_age - 2
    
    # Khloe is a third of Eugene's age.
    eugene_age = khloe_age * 3
    
    # Yorick is twice Eugene’s age.
    yorick_age = eugene_age * 2
    
    # Amilia is a quarter of Yorick’s age.
    amilia_age = yorick_age * 0.25
    
    # Tricia is a third of Amilia’s age.
    tricia_age = amilia_age * 0.33
    
    result = tricia_age
    return result

print(solution())