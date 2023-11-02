def solution():
    # Convert 3 dozen to total balloons
    balloons_on_string = 3 * 12

    # Calculate the number of balloons purchased
    balloons_purchased = 3 + 12

    # Calculate the number of balloons the clown is still holding
    balloons_remaining = balloons_on_string - balloons_purchased
    result = balloons_remaining
    return result

print(solution())