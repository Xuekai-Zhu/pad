def solution():
    """Manny is making lasagna for dinner with his four friends, Lisa, Raphael, Aaron, and Kai. He needs to know how many pieces to cut the lasagna into to serve it. Manny only wants one piece. Aaron doesn't like lasagna much and will probably only eat garlic bread and salad. Kai is always hungry and will eat twice as much as Manny. Raphael always eats half the amount Manny does, but his sister Lisa loves lasagna and will eat two pieces, plus any Raphael has left of his piece. How many pieces should Manny cut his lasagna into?"""
    # Define the number of pieces Manny needs to cut his lasagna into
    manny_pieces = 1

    # Define the amount each person will eat in relation to Manny
    aaron_share = 0.0 # Aaron doesn't like lasagna much and will probably only eat garlic bread and salad
    kai_share = 2.0 # Kai is always hungry and will eat twice as much as Manny
    raphael_share = 0.5 # Raphael always eats half the amount Manny does
    lisa_share = 2.0 # Lisa loves lasagna and will eat two pieces, plus any Raphael has left of his piece

    # Calculate the total number of pieces needed
    total_pieces = manny_pieces + aaron_share + kai_share + raphael_share + lisa_share

    result = total_pieces
    return result

print(solution())