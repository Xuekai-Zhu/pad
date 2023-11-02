def solution():
    """Kaiden and Adriel were to pick a certain number of apples from their farm. After picking 400 apples each, they realized they still had to pick some more, so each picked 3/4 times as many as they had picked earlier. When they checked the pickup truck that was carrying the apples, they found out they still needed to pick 600 apples each to reach the target number. How many apples were they targeting to pick?"""
    # Define the number of apples picked in the first round
    first_round = 400

    # Calculate the number of apples picked in the second round
    second_round = first_round * 3/4

    # Calculate the total number of apples picked by both Kaiden and Adriel before the final pickup
    total_picked = 2 * (first_round + second_round)

    # Calculate the number of apples they still needed to pick
    remaining = 2 * 600

    # Calculate the target number of apples they were supposed to pick
    target = total_picked + remaining

    # Display the target number of apples
    result = target
    return result

print(solution())