def solution():
    """Manny is making lasagna for dinner with his four friends, Lisa, Raphael, Aaron, and Kai. He needs to know how many pieces to cut the lasagna into to serve it. Manny only wants one piece. Aaron doesn't like lasagna much and will probably only eat garlic bread and salad. Kai is always hungry and will eat twice as much as Manny. Raphael always eats half the amount Manny does, but his sister Lisa loves lasagna and will eat two pieces, plus any Raphael has left of his piece. How many pieces should Manny cut his lasagna into?"""
    total_pieces = 0
    total_pieces += 1  # Manny's piece
    total_pieces += 0  # Aaron's piece (garlic bread and salad only)
    total_pieces += 2 + 0.5  # Lisa's pieces + Raphael's piece
    total_pieces += 2 * 1  # Kai's pieces (twice as much as Manny)
    result = total_pieces
    return result

print(solution())