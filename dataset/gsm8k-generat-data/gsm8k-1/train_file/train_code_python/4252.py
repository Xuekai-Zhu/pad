def solution():
    """Joan is preparing sandwiches for a family potluck. She decides to make ham sandwiches and grilled cheese sandwiches.
    One ham sandwich requires 2 slices of cheese, and one grilled cheese sandwich requires 3 slices of cheese.
    She uses a total of 50 slices of cheese to make the sandwiches. If she makes 10 ham sandwiches, how many grilled cheese sandwiches does she make?"""
    ham_cheese_slices = 2
    grilled_cheese_slices = 3
    total_cheese_slices = 50
    ham_sandwiches = 10
    ham_cheese_used = ham_sandwiches * ham_cheese_slices
    grilled_cheese_used = total_cheese_slices - ham_cheese_used
    grilled_cheese_sandwiches = grilled_cheese_used // grilled_cheese_slices
    result = grilled_cheese_sandwiches
    return result

print(solution())