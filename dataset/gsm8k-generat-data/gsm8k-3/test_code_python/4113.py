def solution():
    """Nicholas bought six times as much fabric as Kenneth. If Kenneth paid $40 for an oz of fabric and bought 700oz, calculate the amount of money that Nicholas paid more than Kenneth for the fabric he bought."""
    # Calculate Kenneth's total cost
    kenneth_cost = 40 * 700

    # Calculate Nicholas's total cost
    nicholas_cost = 6 * kenneth_cost

    # Calculate the amount Nicholas paid more than Kenneth
    difference = nicholas_cost - kenneth_cost

    # Display the result
    result = difference
    return result

print(solution())