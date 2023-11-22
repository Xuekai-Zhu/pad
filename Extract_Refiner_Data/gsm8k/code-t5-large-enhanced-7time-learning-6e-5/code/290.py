def solution():
    
    # Define the number of oranges bought
    oranges_bought = 15

    # Calculate the number of oranges washed by each son
    oranges_washed_son1 = oranges_bought - 8
    oranges_washed_son2 = oranges_washed_son1 / 2

    # Calculate the total number of oranges washed
    total_washed = oranges_washed_son1 + oranges_washed_son2

    # Calculate the number of oranges left unwashed
    oranges_unwashed = oranges_bought - total_washed

    # Display the number of oranges left unwashed
    result = oranges_unwashed
    return result

print(solution())