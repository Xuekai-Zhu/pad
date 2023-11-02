def solution():
    
    riverside_kids = 120
    westside_kids = 90
    mountaintop_kids = 50
    denied_riverside = 0.2 * riverside_kids
    denied_westside = 0.7 * westside_kids
    denied_mountaintop = 0.5 * mountaintop_kids
    total_denied = denied_riverside + denied_westside + denied_mountaintop
    total_allowed = (riverside_kids + westside_kids + mountaintop_kids) - total_denied
    result = total_allowed
    return result

print(solution())