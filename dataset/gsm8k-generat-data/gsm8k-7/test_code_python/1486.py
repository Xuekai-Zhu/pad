def solution():
    num_free_haircuts = 5
    haircuts_to_free_one = 14
    haircuts_to_next_free_one = 5

    # Calculate the total number of haircuts Tammy has received
    total_haircuts = (num_free_haircuts + 1) * haircuts_to_free_one - haircuts_to_next_free_one
    result = total_haircuts
    return result

print(solution())