def solution():
    """Nicholas bought six times as much fabric as Kenneth. If Kenneth paid $40 for an oz of fabric and bought 700oz, calculate the amount of money that Nicholas paid more than Kenneth for the fabric he bought."""
    kenneth_fabric = 700
    kenneth_cost = kenneth_fabric * 40
    nicholas_fabric = 6 * kenneth_fabric
    nicholas_cost = nicholas_fabric * 40
    difference = nicholas_cost - kenneth_cost
    result = difference
    return result

print(solution())