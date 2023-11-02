def solution():
    total_earnings = 30  # The girl scouts earned $30 from selling cookies
    cost_per_person = 2.5  # The cost to go to the pool is $2.50 per person
    num_people = 10  # 10 people are going to the pool

    # Calculate the total cost for all the people to go to the pool
    total_cost = cost_per_person * num_people

    # Calculate the amount left after going to the pool
    amount_left = total_earnings - total_cost
    result = amount_left
    return result

print(solution())