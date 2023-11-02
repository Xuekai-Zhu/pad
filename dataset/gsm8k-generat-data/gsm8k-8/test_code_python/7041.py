def solution():
    # Define Elida's and Adrianna's letter counts
    elida_letters = 5
    adrianna_letters = 2 * elida_letters - 2

    # Calculate the average letter count
    average_letters = (elida_letters + adrianna_letters) / 2

    # Calculate 10 times the average letter count
    result = 10 * average_letters
    return result

print(solution())