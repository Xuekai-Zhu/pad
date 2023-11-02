def solution():
    # Define the variables
    red_hats = 6
    blue_boots = 9
    red_hats_and_blue_boots = 3
    total_cookies = red_hats + blue_boots - red_hats_and_blue_boots

    # Calculate the percentage with red hats
    percentage_red_hats = (red_hats / total_cookies) * 100

    result = percentage_red_hats
    return result

print(solution())