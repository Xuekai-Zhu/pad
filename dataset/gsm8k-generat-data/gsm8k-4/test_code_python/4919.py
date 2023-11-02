def solution():
    """Mcdonald is planning to open up a farm that provides eggs to the community. In his local community, Saly needs 10 eggs, Ben needs 14 eggs, and Ked needs half of the number of eggs needed by Ben per week. In a month which has 4 weeks, how many eggs should Mcdonald's farm produce?"""
    # Define the number of eggs needed by Saly and Ben per week
    eggs_saly = 10
    eggs_ben = 14

    # Define the number of eggs needed by Ked per week
    eggs_ked = eggs_ben / 2

    # Calculate the total number of eggs needed per week
    total_eggs_weekly = eggs_saly + eggs_ben + eggs_ked

    # Calculate the total number of eggs needed in a month
    total_eggs_monthly = total_eggs_weekly * 4

    result = total_eggs_monthly
    return result

print(solution())