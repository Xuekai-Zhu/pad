def solution():
    """Luther designs clothes for a high fashion company. His latest line of clothing uses both silk and cashmere fabrics. There are ten pieces made with silk and half that number made with cashmere. If his latest line has thirteen pieces, how many pieces use a blend of cashmere and silk?"""
    # Define the number of silk pieces
    silk_pieces = 10

    # Calculate the number of cashmere pieces
    cashmere_pieces = silk_pieces / 2

    # Calculate the total number of pieces
    total_pieces = 13

    # Calculate the number of pieces with a blend of cashmere and silk
    blend_pieces = total_pieces - silk_pieces - cashmere_pieces

    # Return the result
    result = blend_pieces
    return result

print(solution())