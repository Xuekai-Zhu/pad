def solution():
    """Liz's basketball team is down by 20 points in the final quarter of their game. Liz goes on a shooting spree, sinking 5 free throw shots, 3 three-pointers, and 4 other jump shots. The other team only scores 10 points that quarter, and none of Liz's teammates manage to score any points. How much does Liz's team lose by at the end of the game?"""
    # Define the initial score
    initial_score = 0

    # Calculate Liz's points
    liz_points = 5*1.0 + 3*3.0 + 4*2.0

    # Calculate the other team's points
    other_team_points = 10

    # Calculate Liz's team's final score
    final_score = initial_score + liz_points - other_team_points

    # Calculate the margin of loss
    margin_of_loss = final_score - (-20)

    result = margin_of_loss
    return result

print(solution())