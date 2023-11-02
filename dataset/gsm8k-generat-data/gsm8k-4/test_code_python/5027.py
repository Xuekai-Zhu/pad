def solution():
    """Collin learned that he could earn $0.25 per aluminum can that he brought into the recycling center. He found 12 cans at home and three times as many at his grandparents' house. His neighbor gave him 46. His dad brought home 250 cans from the office. His dad told him he could keep the money from the cans he brought home from the office if he promised to put half of his entire amount collected into savings. How much money would Collin have to put into savings?"""
    # Define the value per can and calculate the total number of cans collected
    CAN_VALUE = 0.25
    total_cans = 12 + 3*12 + 46 + 250

    # Calculate the total value of the cans
    total_value = CAN_VALUE * total_cans

    # Calculate the amount of money Collin gets to keep
    money_kept = (total_value / 2)

    # Return the amount of money Collin has to put into savings
    result = money_kept / 2
    return result

print(solution())