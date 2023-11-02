def solution():
    """Aubrie has four cards with the labels W, X, Y, Z printed on them. W is tagged with the number 200, X is tagged with half the number W is tagged with, Y is tagged with the total of X and W's tags and Z is tagged with the number 400. Calculate the total of all the tagged numbers."""
    W = 200
    X = W / 2
    Y = X + W
    Z = 400
    total = W + X + Y + Z
    result = total
    return result

print(solution())