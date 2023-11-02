def solution():
    """Nicholas bought six times as much fabric as Kenneth. If Kenneth paid $40 for an oz of fabric and bought 700oz, calculate the amount of money that Nicholas paid more than Kenneth for the fabric he bought."""
    # Calculate the amount of fabric that Kenneth bought
    kenneth_fabric = 700

    # Calculate the total cost of the fabric that Kenneth bought
    kenneth_cost = kenneth_fabric * 40

    # Calculate the amount of fabric that Nicholas bought
    nicholas_fabric = kenneth_fabric * 6

    # Calculate the total cost of the fabric that Nicholas bought
    nicholas_cost = nicholas_fabric * 40

    # Calculate the difference in cost between Nicholas and Kenneth
    cost_difference = nicholas_cost - kenneth_cost

    result = cost_difference
    return result

print(solution())