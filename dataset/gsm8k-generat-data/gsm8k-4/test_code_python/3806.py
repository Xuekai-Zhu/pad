def solution():
    """An avant-garde sushi house sells jellyfish for a certain amount and eel for nine times that amount. If the combined cost of one order each kind of sushi is $200, how much does the eel cost?"""
    # Define the cost of jellyfish as x
    x = 1

    # Define the cost of eel as 9x
    eel_cost = 9 * x

    # Calculate the total cost of one order each of jellyfish and eel
    total_cost = x + eel_cost

    # Use the total cost to find the value of x
    x = (200 - eel_cost) / 2

    # Calculate the cost of eel using the new value of x
    eel_cost = 9 * x

    result = round(eel_cost, 2)
    return result

print(solution())