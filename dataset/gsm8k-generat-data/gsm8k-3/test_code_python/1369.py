def solution():
    """A high school bowling team's 3 members scored a total of 810 points in their first match.  
    The first bowler scored 1/3 as many points as the second, and the second bowler scored 3 times as high as the third bowler.  
    How many points did the third bowler score?"""
    # Define the total score and the ratios between the bowlers' scores
    total_score = 810
    first_to_second_ratio = 1/3
    second_to_third_ratio = 3

    # Set up equations for the bowlers' scores
    # Let x be the third bowler's score
    # Then the second bowler's score is 3x, and the first bowler's score is (1/3) * 3x = x
    # The sum of the three scores is 810: x + 3x + x = 810
    # Solving for x:
    x = total_score / 5

    # The third bowler's score is x
    third_bowler_score = x

    # Display the third bowler's score
    result = third_bowler_score
    return result

print(solution())