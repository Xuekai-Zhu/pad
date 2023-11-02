def solution():
    """Annie is a mother of 3 children: Mark, Matt, and Mike. She decided to give them some fruits. Mike received 3 oranges. Matt got twice as many apples, and Mark got as many bananas as Mike and Matt received fruits altogether. How many fruits do the three children have in total?"""
    # Define the number of oranges Mike received
    oranges = 3

    # Calculate the number of apples Matt received, which is twice the number of oranges Mike received
    apples = 2 * oranges

    # Calculate the total number of fruits Mark received, which is the sum of the oranges and apples
    mark_fruits = oranges + apples

    # Calculate the total number of fruits the three children have in total
    total_fruits = oranges + apples + mark_fruits

    # Display the total number of fruits
    result = total_fruits
    return result

print(solution())