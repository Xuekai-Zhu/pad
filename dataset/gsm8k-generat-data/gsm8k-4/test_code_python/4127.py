def solution():
    """Daisy's Flower Shop sold 45 daisies on its first day. On their second day, they sold 20 more flowers than they did on their first day. On the third day, they sold 10 less than twice the flowers that were sold than on the second day. If the flower shop sold a total of 350 daisies for 4 days, how many daisies were sold on the 4th day?"""
    # Define the number of daisies sold on the first day
    day_1 = 45

    # Define the number of daisies sold on the second day
    day_2 = day_1 + 20

    # Define the number of daisies sold on the third day
    day_3 = 2 * day_2 - 10

    # Calculate the total number of daisies sold in 3 days
    total_daisies = day_1 + day_2 + day_3

    # Calculate the number of daisies sold on the fourth day
    day_4 = 350 - total_daisies

    # Return the result
    result = day_4
    return result

print(solution())