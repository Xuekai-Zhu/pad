def solution():
    # Define the two variables: fever and cowbell
    fever = True
    cowbell = False
    # Check if a fever can be cured by listening to a cowbell
    if not cowbell and fever:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())