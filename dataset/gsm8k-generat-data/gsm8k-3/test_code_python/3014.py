def solution():
    """Travis is hired to take 638 bowls from the factory to the home goods store. The home goods store will pay the moving company a $100 fee, plus $3 for every bowl that is delivered safely. Travis must pay the home goods store $4 each for any bowls that are lost or broken. If 12 bowls are lost, 15 bowls are broken, and the rest are delivered safely, how much should Travis be paid?"""
    # Define the price per safe delivery and the cost per lost/broken bowl
    SAFE_PRICE = 3
    LOST_PRICE = 4

    # Get the number of safe and lost/broken bowls
    safe_bowls = 638 - 12 - 15
    lost_bowls = 12 + 15

    # Calculate the total price for the safe deliveries
    safe_price = safe_bowls * SAFE_PRICE

    # Calculate the cost for the lost/broken bowls
    lost_cost = lost_bowls * LOST_PRICE

    # Calculate the total payment for Travis
    payment = 100 + safe_price - lost_cost

    # Display Travis's payment
    result = payment
    return result

print(solution())