def solution():
    """The music festival of Bassompierre begins tonight with a concert by the string orchestra "PIANISSIMO". The ticket price for adults is $26; for children, the price is half. The show starts at 9 pm and goes very well. At about 11:00 pm, the concert organizer made his accounts. There were 183 adults and 28 children who attended the show. What was the total revenue of the concert?"""
    # Define the ticket prices for adults and children
    adult_price = 26
    child_price = adult_price / 2

    # Calculate the total revenue from adult tickets
    adult_revenue = adult_price * 183

    # Calculate the total revenue from child tickets
    child_revenue = child_price * 28

    # Calculate the total revenue
    total_revenue = adult_revenue + child_revenue

    # return the result
    result = total_revenue
    return result

print(solution())