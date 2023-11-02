def solution():
    """Purple Valley has one-quarter as many skirts as Seafoam Valley, and Seafoam Valley has two-thirds as many skirts as Azure Valley. If Azure Valley has 60 skirts, how many skirts does Purple Valley have?"""
    azure_skirts = 60
    seafoam_skirts = azure_skirts * (2/3)
    purple_skirts = seafoam_skirts * (1/4)
    result = purple_skirts
    return result

print(solution())