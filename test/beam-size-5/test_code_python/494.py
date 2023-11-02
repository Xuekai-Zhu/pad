def solution():
    # Calculate the total number of oranges Ashley brought
    ashley_oranges = 5 * 10

    # Calculate the total number of oranges Brianne brought
    brianne_oranges = ashley_oranges + 20

    # Calculate the total number of oranges they can make
    total_oranges = ashley_oranges + brianne_oranges

    # Calculate the number of greek orange pies they can make
    greek_orange_pies = total_oranges // 3

    result = greek_orange_pies
    return result

print(solution())