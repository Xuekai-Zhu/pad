def solution():

    # Define the relationships between the ages
    eugene_age = 11  # Khloe is 1/3 of Eugene's age
    khloe_age = eugene_age / 3
    yorick_age = 4 * eugene_age  # Amilia is 1/4 of Yorick's age
    amilia_age = yorick_age / 4
    tricia_age = amilia_age / 3

    # Calculate Rupert's age
    vincent_age = 22
    rupert_age = vincent_age + 10

    result = tricia_age
    return result

print(solution())