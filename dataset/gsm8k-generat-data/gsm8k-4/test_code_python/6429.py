def solution():
    """
    Arnold's collagen powder has 18 grams of protein for every 2 scoops. His protein powder has 21 grams of protein per scoop. 
    And his steak has 56 grams of protein. If he has 1 scoop of collagen powder, 1 scoop of protein powder and his steak, 
    how many grams of protein will he consume?
    """
    # Define the protein content of each type of food
    collagen_protein = 18 / 2  # 9 grams of protein per scoop
    protein_powder_protein = 21  # 21 grams of protein per scoop
    steak_protein = 56

    # Calculate the total protein intake
    total_protein = collagen_protein + protein_powder_protein + steak_protein

    result = total_protein
    return result

print(solution())