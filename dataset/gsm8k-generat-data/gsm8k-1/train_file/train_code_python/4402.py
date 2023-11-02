def solution():
    """
    Manny is making lasagna for dinner with his four friends, Lisa, Raphael, Aaron, and Kai. He needs to know how many 
    pieces to cut the lasagna into to serve it. Manny only wants one piece. Aaron doesn't like lasagna much and will 
    probably only eat garlic bread and salad. Kai is always hungry and will eat twice as much as Manny. Raphael always 
    eats half the amount Manny does, but his sister Lisa loves lasagna and will eat two pieces, plus any Raphael has 
    left of his piece. How many pieces should Manny cut his lasagna into?
    """
    total_people = 5
    aaron = 0.5
    kai = 2
    raphael = 0.5
    lisa = 2
    manny = 1
    total_lasagna = aaron + kai + raphael + lisa + manny
    result = total_lasagna
    return result

print(solution())