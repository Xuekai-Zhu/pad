def solution():
    """Tricia is a third of Amilia’s age and Amilia is a quarter of Yorick’s age. Yorick is twice Eugene’s age and Khloe is a third of Eugene’s age. Rupert is 10 years older than Khloe but 2 years younger than Vincent who is 22 years old. How old, in years, is Tricia?"""
    # Define the relationships between the ages
    eugene_age = 11  # given that Khloe is a third of Eugene's age
    yorick_age = 2 * eugene_age  # given that Yorick is twice Eugene's age
    amilia_age = yorick_age / 4  # given that Amilia is a quarter of Yorick's age
    tricia_age = amilia_age / 3  # given that Tricia is a third of Amilia's age
    rupert_age = eugene_age / 3 + 10  # given that Rupert is 10 years older than Khloe
    vincent_age = rupert_age + 2  # given that Vincent is 22 years old

    # Display Tricia's age
    result = tricia_age
    return result

print(solution())