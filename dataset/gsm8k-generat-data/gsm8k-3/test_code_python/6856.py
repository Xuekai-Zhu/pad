def solution():
    """Of the 600 students at River Falls High School, 3/4 of them play tennis. Of those that play tennis, 60% of them also play hockey. How many students play both hockey and tennis?"""
    
    # Calculate the number of students that play tennis
    tennis_players = 600 * (3/4)

    # Calculate the number of tennis players that also play hockey
    hockey_and_tennis_players = tennis_players * 0.6

    # Display the number of students that play both hockey and tennis
    result = hockey_and_tennis_players
    return result

print(solution())