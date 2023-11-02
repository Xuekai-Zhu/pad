def solution():
    """Ginger is weaving mats out of colored straw. Each mat takes 20 red straws, 30 orange straws, and half as many green straws as orange straws. How many straws does she need to make 10 mats?"""
    # Define the number of straws needed for each color
    red_straws_per_mat = 20
    orange_straws_per_mat = 30
    green_straws_per_mat = orange_straws_per_mat / 2

    # Calculate the total number of straws needed to make 10 mats
    total_straws = (red_straws_per_mat + orange_straws_per_mat + green_straws_per_mat) * 10

    # return the result
    result = total_straws
    return result

print(solution())