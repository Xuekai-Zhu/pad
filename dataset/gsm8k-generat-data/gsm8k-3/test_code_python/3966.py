def solution():
    """Luther designs clothes for a high fashion company. His latest line of clothing uses both silk and cashmere fabrics. There are ten pieces made with silk and half that number made with cashmere. If his latest line has thirteen pieces, how many pieces use a blend of cashmere and silk?"""
    # Define the number of pieces made with silk and cashmere
    silk_pieces = 10
    cashmere_pieces = silk_pieces / 2

    # Calculate the number of pieces that use a blend of cashmere and silk
    blend_pieces = 13 - silk_pieces - cashmere_pieces

    # Display the number of pieces that use a blend of cashmere and silk
    result = blend_pieces
    return result

print(solution())