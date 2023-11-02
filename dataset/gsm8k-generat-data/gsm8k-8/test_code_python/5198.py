def solution():
    # Define the initial number of pairs that Lisa bought
    lisa_bought = 12

    # Define the number of pairs that Sandra brought
    sandra_brought = 20

    # Define the number of pairs that Lisa's cousin brought
    cousin_brought = sandra_brought / 5

    # Define the number of pairs that Lisa's mom brought
    mom_brought = 3 * lisa_bought + 8

    # Calculate the total number of pairs Lisa has
    total_pairs = lisa_bought + sandra_brought + cousin_brought + mom_brought
    result = total_pairs
    return result

print(solution())