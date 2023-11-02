def solution():
    """Scott, Mary, and Ken committed to raising $4,000 for their local children’s cancer hospital. Right now, Mary’s collection is five times what Ken has, but three times Scott’s funds. If Ken has $600, by how much have the three exceeded their goal?"""
    # Set Ken's funds
    ken_funds = 600

    # Calculate Mary's funds and Scott's funds
    mary_funds = 5 * ken_funds
    scott_funds = mary_funds / 3

    # Calculate the total funds raised by the three
    total_funds = mary_funds + scott_funds + ken_funds

    # Calculate the amount exceeded from the goal
    excess = total_funds - 4000

    # Display the excess amount
    result = excess
    return result

print(solution())