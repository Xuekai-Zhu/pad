def solution():
    """An ice cream vendor has 50 chocolate-flavored ice creams and 54 mango-flavored ice creams in his cart. If he sold 3/5 of the chocolate-flavored ice creams and 2/3 of the mango-flavored ice creams, how many total ice creams were not sold?"""
    # Calculate the number of chocolate ice creams sold
    chocolate_sold = int(3/5*50)

    # Calculate the number of mango ice creams sold
    mango_sold = int(2/3*54)

    # Calculate the total number of ice creams not sold
    total_not_sold = 50 - chocolate_sold + 54 - mango_sold

    # Display the total number of ice creams not sold
    result = total_not_sold
    return result

print(solution())