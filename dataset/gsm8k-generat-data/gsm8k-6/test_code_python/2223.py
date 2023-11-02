def solution():
    # Calculate the number of pieces of gum that Elyse gave to her brother Rick
    pieces_to_rick = 100/2  

    # Calculate the number of pieces of gum that Rick gave to his friend Shane
    pieces_to_shane = pieces_to_rick/2  

    # Calculate the number of pieces of gum that Shane has left
    pieces_left = pieces_to_shane - 11

    result = pieces_left
    return result

print(solution())