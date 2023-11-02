def solution():
    """Florida is starting a promotion where every car that arrives gets one orange per passenger. A family of 4 arrives and gets their oranges. They had planned to stop for a snack later where they would spend $15 in total, but now that they have the oranges they don't have to buy them at the stop. When they get to the stop they see that the oranges would've cost $1.5 each. What percentage of the money they planned to spend did they save instead?"""
    # Calculate the total cost of oranges at the stop
    orange_cost = 1.5 * 4 # 4 passengers in the family

    # Calculate the amount the family saved by not buying oranges at the stop
    saved_money = orange_cost

    # Calculate the percentage of the money they planned to spend that they saved
    percentage_saved = (saved_money / 15) * 100

    # Display the percentage saved
    result = percentage_saved
    return result

print(solution())