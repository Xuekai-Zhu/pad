def solution():
    """Susan earned $600 from babysitting over the summer. She went shopping and spent half of it on clothes. Then she spent half of what was left on books. How much money did she have left?"""
    # Define Susan's earnings
    earnings = 600

    # Calculate the amount spent on clothes
    clothes_cost = earnings / 2

    # Calculate the amount left after buying clothes
    remaining_money = earnings - clothes_cost

    # Calculate the amount spent on books
    books_cost = remaining_money / 2

    # Calculate the amount left after buying books
    total_left = remaining_money - books_cost

    # Display the amount of money Susan has left
    result = total_left
    return result

print(solution())