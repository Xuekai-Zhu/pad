def solution():
    """Manny is making lasagna for dinner with his four friends, Lisa, Raphael, Aaron, and Kai. He needs to know how many pieces to cut the lasagna into to serve it. Manny only wants one piece. Aaron doesn't like lasagna much and will probably only eat garlic bread and salad. Kai is always hungry and will eat twice as much as Manny. Raphael always eats half the amount Manny does, but his sister Lisa loves lasagna and will eat two pieces, plus any Raphael has left of his piece. How many pieces should Manny cut his lasagna into?"""
    # Define the number of pieces Manny needs to cut the lasagna into
    manny_pieces = 1

    # Define the number of pieces Aaron will eat
    aaron_pieces = 0

    # Define the number of pieces Kai will eat
    kai_pieces = manny_pieces * 2

    # Define the number of pieces Raphael will eat
    raphael_pieces = manny_pieces / 2

    # Define the number of pieces Lisa will eat
    lisa_pieces = raphael_pieces * 2 + 2

    # Calculate the total number of pieces needed
    total_pieces = manny_pieces + aaron_pieces + kai_pieces + raphael_pieces + lisa_pieces

    # Display the total number of pieces needed
    result = total_pieces
    return result

print(solution())