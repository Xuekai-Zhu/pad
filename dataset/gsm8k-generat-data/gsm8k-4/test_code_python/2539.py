def solution():
    """Florida is starting a promotion where every car that arrives gets one orange per passenger. A family of 4 arrives and gets their oranges. They had planned to stop for a snack later where they would spend $15 in total, but now that they have the oranges they don't have to buy them at the stop. When they get to the stop they see that the oranges would've cost $1.5 each. What percentage of the money they planned to spend did they save instead?"""
    # Define the number of oranges received
    oranges_received = 4

    # Calculate the cost of the oranges that they don't have to buy at the stop
    oranges_cost = oranges_received * 1.5

    # Calculate the percentage of the planned spending that they saved
    saved_percentage = (oranges_cost / 15) * 100

    # return the result
    result = saved_percentage
    return result

print(solution())