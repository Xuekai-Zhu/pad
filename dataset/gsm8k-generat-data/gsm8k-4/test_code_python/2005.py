def solution():
    """Hazel put up a lemonade stand. She sold half her lemonade to a construction crew. She sold 18 cups to kids on bikes. She gave away half that amount to her friends. Then she drank the last cup of lemonade herself. How many cups of lemonade did Hazel make?"""
    # Define the number of cups Hazel sold to the construction crew
    sold_to_crew = None

    # Define the number of cups Hazel sold to kids on bikes
    sold_to_kids = 18

    # Define the number of cups Hazel gave away
    given_away = sold_to_kids / 2

    # Define the total number of cups Hazel made
    total_cups = sold_to_crew + sold_to_kids + given_away + 1

    # Return the result
    result = total_cups
    return result

print(solution())