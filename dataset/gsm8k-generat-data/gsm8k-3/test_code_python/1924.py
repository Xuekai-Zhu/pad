def solution():
    """Taro and Vlad play a video game competition together, earning 5 points for every win. After playing 30 rounds, Taro scored 4 points less than 3/5 of the total points scored. How many total points did Vlad score?"""
    # Define the points earned per win
    POINTS_PER_WIN = 5

    # Calculate the total number of points scored in the 30 rounds
    total_points = POINTS_PER_WIN * 30

    # Calculate Taro's score
    taro_score = (3/5) * total_points - 4

    # Calculate Vlad's score
    vlad_score = total_points - taro_score

    # Display Vlad's score
    result = vlad_score
    return result

print(solution())