def solution():
    """Sammy has 2 more bottle caps than Janine. Janine has 3 times as many bottle caps as Billie. If Billie has 2 bottle caps, how many does Sammy have?"""
    billie_caps = 2
    janine_caps = 3 * billie_caps
    sammy_caps = janine_caps + 2
    result = sammy_caps
    return result

print(solution())