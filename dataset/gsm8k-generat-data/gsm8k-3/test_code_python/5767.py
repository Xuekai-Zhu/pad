def solution():
    """Jefferson has 56 bananas, while Walter, his friend, has 1/4 times fewer bananas. If they decide to combine their bananas and share them equally between themselves, how many bananas does Walter get?"""
    # Define the number of bananas Jefferson has
    jefferson_bananas = 56

    # Calculate the number of bananas Walter has
    walter_bananas = jefferson_bananas - (jefferson_bananas / 4)

    # Calculate the total number of bananas they have when combined
    total_bananas = jefferson_bananas + walter_bananas

    # Calculate the number of bananas each person gets when they split them equally
    bananas_per_person = total_bananas / 2

    # Display the number of bananas Walter gets
    result = bananas_per_person - jefferson_bananas / 2
    return result

print(solution())