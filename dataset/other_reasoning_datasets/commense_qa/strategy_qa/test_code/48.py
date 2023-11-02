def solution():
    HS1_length = 108 # in km
    CERN_tunnel_circumference = 26.7 # in km
    # Convert CERN tunnel circumference to length using the formula L = 2*pi*r
    CERN_tunnel_length = 2 * 3.14159 * (CERN_tunnel_circumference / (2 * 3.14159))
    if CERN_tunnel_length <= HS1_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())