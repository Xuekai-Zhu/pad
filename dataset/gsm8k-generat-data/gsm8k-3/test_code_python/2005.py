def solution():
    """Hazel put up a lemonade stand. She sold half her lemonade to a construction crew. She sold 18 cups to kids on bikes. She gave away half that amount to her friends. Then she drank the last cup of lemonade herself. How many cups of lemonade did Hazel make?"""
    # Calculate the number of cups sold to the construction crew
    cups_sold = 18 * 2

    # Calculate the number of cups given away to friends
    cups_given_away = cups_sold / 2

    # Calculate the total number of cups Hazel made
    total_cups = cups_sold + cups_given_away + 1  # add 1 for the cup she drank

    # Display the total number of cups Hazel made
    result = total_cups
    return result

print(solution())