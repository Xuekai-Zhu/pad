def solution():
    """The girl scouts earned $30 total from selling delicious cookies. They want to go to the pool. It will cost them $2.50 per person to go and 10 people are going. What is the amount left?"""
    # Define the amount earned
    earned = 30

    # Define the cost per person and the number of people going to the pool
    cost_per_person = 2.5
    num_people = 10

    # Calculate the total cost of going to the pool
    total_cost = cost_per_person * num_people

    # Calculate the amount left after going to the pool
    amount_left = earned - total_cost

    # Display the amount left
    result = amount_left
    return result

print(solution())