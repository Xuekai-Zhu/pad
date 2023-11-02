def solution():
    """Jenny wants to sell some girl scout cookies and has the choice of two neighborhoods to visit. Neighborhood A has 10 homes
    which each will buy 2 boxes of cookies. Neighborhood B has 5 homes, each of which will buy 5 boxes of cookies. Assuming each box 
    of cookies costs $2, how much will Jenny make at the better choice of the two neighborhoods?"""
    
    # Define the number of homes and boxes of cookies in each neighborhood
    homes_A = 10
    boxes_A = 2
    homes_B = 5
    boxes_B = 5

    # Calculate the total earnings in each neighborhood
    earnings_A = homes_A * boxes_A * 2
    earnings_B = homes_B * boxes_B * 2

    # Choose the neighborhood with the higher earnings
    if earnings_A > earnings_B:
        neighborhood = "A"
        earnings = earnings_A
    else:
        neighborhood = "B"
        earnings = earnings_B
    
    result = earnings
    return result

print(solution())