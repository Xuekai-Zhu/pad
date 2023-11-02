def solution():
    # Calculate total cost of admission for Kath and her group
    cost_before_6pm = 8 - 3  # cost of admission before 6 PM
    num_people = 2 + 3  # Kath's siblings and 3 friends
    total_cost = (cost_before_6pm * num_people)  # cost for all of them to watch the movie before 6 PM
    result = total_cost
    return result

print(solution())