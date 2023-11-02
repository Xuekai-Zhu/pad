def solution():
    """Aubrie has four cards with the labels W, X, Y, Z printed on them. W is tagged with the number 200, X is tagged with half the number W is tagged with, Y is tagged with the total of X and W's tags and Z is tagged with the number 400. Calculate the total of all the tagged numbers."""
    w_tag = 200
    x_tag = w_tag / 2
    y_tag = w_tag + x_tag
    z_tag = 400
    total = w_tag + x_tag + y_tag + z_tag
    result = total
    return result

print(solution())