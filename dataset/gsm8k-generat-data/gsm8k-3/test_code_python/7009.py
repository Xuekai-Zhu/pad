def solution():
    """Pablo’s mother agrees to pay him one cent for every page he reads. He plans to save the money for some candy. Pablo always checks out books that are exactly 150 pages. After reading his books, he went to the store and bought $15 worth of candy and had $3 leftover. How many books did Pablo read?"""
    # Define the cost of candy and the amount of money Pablo had left over
    CANDY_COST = 15
    LEFTOVER_MONEY = 3

    # Define the amount of money Pablo earned from reading
    EARNED_MONEY = 0.01 * 150

    # Calculate the total amount of money Pablo earned
    total_money = (CANDY_COST + LEFTOVER_MONEY) / EARNED_MONEY

    # Calculate the number of books Pablo read
    num_books = int(total_money / 150)

    # Display the number of books Pablo read
    result = num_books
    return result

print(solution())