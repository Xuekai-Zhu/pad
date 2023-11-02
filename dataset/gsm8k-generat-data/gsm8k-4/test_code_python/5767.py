def solution():
    """Jefferson has 56 bananas, while Walter, his friend, has 1/4 times fewer bananas.
    If they decide to combine their bananas and share them equally between themselves,
    how many bananas does Walter get?"""
    # Define the number of bananas Jefferson has
    jefferson_bananas = 56

    # Calculate the number of bananas Walter has
    walter_bananas = jefferson_bananas - jefferson_bananas * (1/4)

    # Calculate the total number of bananas
    total_bananas = jefferson_bananas + walter_bananas

    # Calculate the number of bananas each person gets
    per_person_bananas = total_bananas / 2

    # Determine how many bananas Walter gets
    walter_gets = per_person_bananas - walter_bananas

    # Return the result
    result = walter_gets
    return result

print(solution())