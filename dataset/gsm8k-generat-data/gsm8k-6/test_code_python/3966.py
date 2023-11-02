def solution():
    # Calculate the number of pieces made with cashmere
    cashmere_pieces = 10/2  # half the number of pieces made with silk
    # Calculate the number of pieces made with both cashmere and silk
    blend_pieces = 13 - 10 - cashmere_pieces  # total pieces minus silk pieces minus cashmere pieces
    result = blend_pieces
    return result

print(solution())