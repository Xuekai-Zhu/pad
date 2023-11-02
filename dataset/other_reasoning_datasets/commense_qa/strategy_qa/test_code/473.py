def solution():
    # Define the properties of Judo and Silicone
    requires_gripping = True
    silicone_slipperiness = True
    # Check if silicone suits make Judo difficult
    if requires_gripping and silicone_slipperiness:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())