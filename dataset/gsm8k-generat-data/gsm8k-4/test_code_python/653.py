def solution():
    """Fred spent half of his allowance going to the movies. He washed the family car and earned 6 dollars. What is his weekly allowance if he ended with 14 dollars?"""
    # Define the variables
    allowance = None
    movie_spending = None
    car_washing = 6
    ending_balance = 14

    # Calculate the spending on the movies
    movie_spending = (ending_balance - car_washing) * 0.5

    # Calculate the total allowance
    allowance = (ending_balance - car_washing) + (2 * movie_spending)

    result = allowance
    return result

print(solution())