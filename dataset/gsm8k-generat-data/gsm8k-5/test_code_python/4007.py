def solution():
    free_throws = 5  # Liz makes 5 free throw shots worth 1 point each
    three_pointers = 3  # Liz makes 3 three-pointers worth 3 points each
    jump_shots = 4  # Liz makes 4 jump shots worth 2 points each
    Liz_score = (free_throws * 1) + (three_pointers * 3) + (jump_shots * 2)  # Liz's total score in the final quarter
    opposing_score = 10  # The other team scores 10 points in the final quarter
    point_deficit = 20  # Liz's team is down by 20 points at the start of the final quarter

    # Calculate how much Liz's team loses by at the end of the game
    total_deficit = point_deficit - (Liz_score - opposing_score)
    result = total_deficit
    return result

print(solution())