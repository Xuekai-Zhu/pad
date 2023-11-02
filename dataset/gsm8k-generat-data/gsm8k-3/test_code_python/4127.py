def solution():
    """Daisy's Flower Shop sold 45 daisies on its first day. On their second day, they sold 20 more flowers than they did on their first day. On the third day, they sold 10 less than twice the flowers that were sold than on the second day. If the flower shop sold a total of 350 daisies for 4 days, how many daisies were sold on the 4th day?"""
    # Define the number of daisies sold on the first day
    daisies_1 = 45

    # Calculate the number of daisies sold on the second day
    daisies_2 = daisies_1 + 20

    # Calculate the number of daisies sold on the third day
    daisies_3 = 2 * daisies_2 - 10

    # Calculate the total number of daisies sold in the first three days
    total_daisies = daisies_1 + daisies_2 + daisies_3

    # Calculate the number of daisies sold on the fourth day
    daisies_4 = 350 - total_daisies

    # Display the number of daisies sold on the fourth day
    result = daisies_4
    return result

print(solution())