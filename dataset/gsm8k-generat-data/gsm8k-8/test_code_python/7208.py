def solution():
    # Calculate the total number of puppies
    total_puppies = 2 * 10

    # Calculate the number of puppies sold
    puppies_sold = int((3/4) * total_puppies)

    # Calculate the total amount received from selling the puppies
    total_amount = puppies_sold * 200

    result = total_amount
    return result

print(solution())