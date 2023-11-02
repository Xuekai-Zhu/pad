def solution():
    """Jenny wants to sell some girl scout cookies and has the choice of two neighborhoods to visit. Neighborhood A has 10 homes which each will buy 2 boxes of cookies. Neighborhood B has 5 homes, each of which will buy 5 boxes of cookies. Assuming each box of cookies costs $2, how much will Jenny make at the better choice of the two neighborhoods?"""
    neighborhood_A_homes = 10
    neighborhood_A_boxes = 2
    neighborhood_B_homes = 5
    neighborhood_B_boxes = 5
    price_per_box = 2

    total_money_A = neighborhood_A_homes * neighborhood_A_boxes * price_per_box
    total_money_B = neighborhood_B_homes * neighborhood_B_boxes * price_per_box

    result = max(total_money_A, total_money_B)
    return result

print(solution())