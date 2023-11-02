def solution():
    """Calvin and Paislee played a pool game where points were awarded for winning a round. If Calvin had scored 500 points and Paislee 3/4 times as many points as Calvin, how many points was Paislee required to achieve to have a chance of tying the game?"""
    # Define Calvin's score
    calvin_score = 500

    # Calculate Paislee's score
    paislee_score = calvin_score * 0.75

    # Calculate the minimum score Paislee needs to tie the game with Calvin
    tie_score = calvin_score - paislee_score + 1

    # Display the minimum score needed for a tie
    result = tie_score
    return result

print(solution())