def solution():
    """The girl scouts earned $30 total from selling delicious cookies. They want to go to the pool. It will cost them $2.50 per person to go and 10 people are going. What is the amount left?"""
    # Define the total earnings from selling cookies and the cost per person to go to the pool
    total_earnings = 30
    cost_per_person = 2.5

    # Define the number of people going to the pool
    num_people = 10

    # Calculate the total cost of going to the pool
    total_cost = cost_per_person * num_people

    # Calculate the amount left after going to the pool
    amount_left = total_earnings - total_cost

    # Return the amount left
    result = amount_left
    return result

print(solution())