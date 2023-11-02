def solution():
    """Purple Valley has one-quarter as many skirts as Seafoam Valley, and Seafoam Valley has two-thirds as many skirts as Azure Valley. If Azure Valley has 60 skirts, how many skirts does Purple Valley have?"""
    # Define the number of skirts in Azure Valley
    azure_skirts = 60

    # Calculate the number of skirts in Seafoam Valley
    seafoam_skirts = azure_skirts * (2/3)

    # Calculate the number of skirts in Purple Valley
    purple_skirts = seafoam_skirts * (1/4)

    # Display the number of skirts in Purple Valley
    result = purple_skirts
    return result

print(solution())