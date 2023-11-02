def solution():
    """The girl scouts earned $30 total from selling delicious cookies. They want to go to the pool. It will cost them $2.50 per person to go and 10 people are going. What is the amount left?"""
    total_earned = 30
    cost_per_person = 2.5
    num_people = 10
    total_cost = cost_per_person * num_people
    amount_left = total_earned - total_cost
    result = amount_left
    return result

print(solution())