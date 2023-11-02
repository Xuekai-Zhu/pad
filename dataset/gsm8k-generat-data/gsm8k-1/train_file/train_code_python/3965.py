def solution():
    """Luther designs clothes for a high fashion company. His latest line of clothing uses both silk and cashmere fabrics. There are ten pieces made with silk and half that number made with cashmere. If his latest line has thirteen pieces, how many pieces use a blend of cashmere and silk?"""
    silk_pieces = 10
    cashmere_pieces = silk_pieces / 2
    total_pieces = 13
    blend_pieces = total_pieces - silk_pieces - cashmere_pieces
    result = blend_pieces
    return result

print(solution())