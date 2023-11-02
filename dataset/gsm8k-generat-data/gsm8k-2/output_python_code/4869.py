def solution():
    """The music festival of Bassompierre begins tonight with a concert by the string orchestra "PIANISSIMO". The ticket price for adults is $26; for children, the price is half. The show starts at 9 pm and goes very well. At about 11:00 pm, the concert organizer made his accounts. There were 183 adults and 28 children who attended the show. What was the total revenue of the concert?"""
    adult_price = 26
    child_price = adult_price / 2
    adult_tickets = 183
    child_tickets = 28
    total_revenue = (adult_tickets * adult_price) + (child_tickets * child_price)
    result = total_revenue
    return result

print(solution())