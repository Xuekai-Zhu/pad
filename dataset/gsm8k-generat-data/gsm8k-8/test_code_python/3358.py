def solution():
    # Define the number of nose sprays Bob buys
    num_sprays = 10

    # Calculate the total number of nose sprays Bob receives
    total_sprays = num_sprays * 2

    # Calculate the total cost of the nose sprays
    total_cost = num_sprays * 3

    # Calculate the amount Bob saves with the promotion
    saved_cost = num_sprays * 1.5

    # Calculate the final cost Bob pays
    final_cost = total_cost - saved_cost
    result = final_cost
    return result

print(solution())