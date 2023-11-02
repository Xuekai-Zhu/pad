def solution():
    # Calculate the total number of puppies
    total_puppies = 3 * 4  # 3 pregnant dogs give birth to 4 puppies each

    # Calculate the total number of shots needed for all the puppies
    total_shots = total_puppies * 2  # each puppy needs 2 shots

    # Calculate the total cost of the shots
    total_cost = total_shots * 5  # each shot costs $5

    result = total_cost
    return result

print(solution())