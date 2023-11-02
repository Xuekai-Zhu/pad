def solution():
    """Sara’s house is 100 square feet larger than 2 times Nada's house. If Sara's house is 1000 square feet, how many square feet is Nada's house?"""
    # Define the area of Sara's house and the relation between the areas
    sara_area = 1000
    sara_relation = 2

    # Calculate the area of Nada's house
    nada_area = (sara_area - 100) / sara_relation

    # Display the area of Nada's house
    result = nada_area
    return result

print(solution())