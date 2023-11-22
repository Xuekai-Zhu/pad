def solution():
    
    # Define the initial amount of money Raymond had
    initial_money = 21

    # Define the amount of money Raymond saved
    savings = 11

    # Define the amount of money Raymond spent on the comic book and puzzle
    book_cost = 5
    puzzle_cost = 19

    # Calculate the total amount of money Raymond has left
    remaining_money = initial_money + savings - book_cost - puzzle_cost

    # Display the remaining amount of money Raymond has left
    result = remaining_money
    return result

print(solution())