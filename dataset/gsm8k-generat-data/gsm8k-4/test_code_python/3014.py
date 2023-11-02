def solution():
    """Travis is hired to take 638 bowls from the factory to the home goods store. The home goods store will pay the moving company a $100 fee, plus $3 for every bowl that is delivered safely. Travis must pay the home goods store $4 each for any bowls that are lost or broken. If 12 bowls are lost, 15 bowls are broken, and the rest are delivered safely, how much should Travis be paid?"""
    # Define the number of bowls to move
    bowls_to_move = 638

    # Calculate the number of bowls delivered safely
    bowls_delivered_safely = bowls_to_move - 12 - 15

    # Calculate the total amount paid by the home goods store for safely delivered bowls
    home_goods_payment = bowls_delivered_safely * 3

    # Calculate the total amount paid by Travis for lost or broken bowls
    travis_payment = (12 + 15) * 4

    # Calculate the total amount Travis should be paid
    total_payment = home_goods_payment + 100 - travis_payment

    result = total_payment
    return result

print(solution())