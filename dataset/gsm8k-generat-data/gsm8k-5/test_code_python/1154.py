def solution():
    num_grandchildren = 5
    num_children = 4
    num_stockings_per_person = 5
    stocking_cost = 20 * 0.9  # The stockings are 10% off
    monogramming_cost = 5

    # Calculate the total cost of the stockings
    total_stocking_cost = (num_grandchildren + num_children) * num_stockings_per_person * stocking_cost

    # Calculate the total cost of the monogramming
    total_monogramming_cost = (num_grandchildren + num_children) * num_stockings_per_person * monogramming_cost

    # Calculate the final cost of the stockings
    final_cost = total_stocking_cost + total_monogramming_cost
    result = final_cost
    return result

print(solution())