def solution():
    """Sammy has 2 more bottle caps than Janine. Janine has 3 times as many bottle caps as Billie. If Billie has 2 bottle caps, how many does Sammy have?"""
    # Define the number of bottle caps for Billie
    billie_caps = 2

    # Calculate the number of bottle caps for Janine
    janine_caps = billie_caps * 3

    # Calculate the number of bottle caps for Sammy
    sammy_caps = janine_caps + 2

    # Display the number of bottle caps for Sammy
    result = sammy_caps
    return result

print(solution())