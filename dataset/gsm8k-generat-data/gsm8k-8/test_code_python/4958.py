def solution():
    # Calculate the total number of roses sold
    roses_sold = 10 * 12

    # Calculate the total number of flowers sold
    total_flowers_sold = 190

    # Calculate the total number of daisies sold
    daisies_sold = total_flowers_sold - roses_sold

    # Calculate the number of daisies in each bouquet of daisies
    daisies_in_bouquet = daisies_sold / 10
    result = daisies_in_bouquet
    return result

print(solution())