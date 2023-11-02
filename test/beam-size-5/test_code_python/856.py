def solution():
    
    # Define the initial number of oranges
    initial_oranges = 12

    # Calculate the number of oranges given to the daughters
    daughters_oranges = 3 * 2

    # Calculate the total number of oranges given away
    total_given_away = daughters_oranges + 3

    # Calculate the number of oranges left with
    oranges_left = initial_oranges - total_given_away

    # Display the number of oranges left with
    result = oranges_left
    return result

print(solution())