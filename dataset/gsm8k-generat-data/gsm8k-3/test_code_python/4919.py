def solution():
    """Mcdonald is planning to open up a farm that provides eggs to the community. In his local community, Saly needs 10 eggs, Ben needs 14 eggs, and Ked needs half of the number of eggs needed by Ben per week. In a month which has 4 weeks, how many eggs should Mcdonald's farm produce?"""
    # Define the number of eggs needed by each person per week
    SALY_WEEKLY = 10
    BEN_WEEKLY = 14
    KED_WEEKLY = BEN_WEEKLY / 2

    # Calculate the total number of eggs needed per week
    total_weekly = SALY_WEEKLY + BEN_WEEKLY + KED_WEEKLY

    # Calculate the total number of eggs needed per month
    total_monthly = total_weekly * 4

    # Display the total number of eggs needed per month
    result = total_monthly
    return result

print(solution())