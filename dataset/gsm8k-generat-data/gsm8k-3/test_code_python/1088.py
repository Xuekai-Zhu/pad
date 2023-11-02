def solution():
    """We the People has 17 cows. Happy Good Healthy Family has two more than three times the number of cows We the People has. If their cows are taken to a ranch to graze together, how many cows will be in the ranch altogether?"""
    # Define the number of cows We the People has
    we_the_people_cows = 17

    # Calculate the number of cows Happy Good Healthy Family has
    happy_good_healthy_cows = 3 * we_the_people_cows + 2

    # Calculate the total number of cows on the ranch
    total_cows = we_the_people_cows + happy_good_healthy_cows

    # Display the total number of cows on the ranch
    result = total_cows
    return result

print(solution())