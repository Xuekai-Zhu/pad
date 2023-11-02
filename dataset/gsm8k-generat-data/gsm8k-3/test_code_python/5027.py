def solution():
    """Collin learned that he could earn $0.25 per aluminum can that he brought into the recycling center. He found 12 cans at home and three times as many at his grandparents' house. His neighbor gave him 46. His dad brought home 250 cans from the office. His dad told him he could keep the money from the cans he brought home from the office if he promised to put half of his entire amount collected into savings. How much money would Collin have to put into savings?"""
    # Define the amount earned per aluminum can
    CAN_PRICE = 0.25

    # Calculate the number of cans Collin collected
    home_cans = 12
    grandparent_cans = 3 * home_cans
    neighbor_cans = 46
    dad_cans = 250

    total_cans = home_cans + grandparent_cans + neighbor_cans + dad_cans

    # Calculate the total amount earned from recycling
    total_earnings = total_cans * CAN_PRICE

    # Calculate the amount to put into savings
    savings_amount = total_earnings / 2

    # Display the amount to put into savings
    result = savings_amount
    return result

print(solution())