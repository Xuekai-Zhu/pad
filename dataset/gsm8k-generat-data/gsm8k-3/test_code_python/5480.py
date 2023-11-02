def solution():
    """Helga works for a newspaper company. She can write 5 articles every 30 minutes, and she usually works 4 hours a day 5 days a week. If Helga worked an extra 2 hours last Thursday, and an extra 3 hours last Friday, how many articles was she able to write this week?"""
    # Define Helga's writing rate
    WRITING_RATE = 5 / 0.5 # 5 articles in 30 minutes

    # Define Helga's regular hours
    REGULAR_HOURS = 4 * 5 # 4 hours a day, 5 days a week

    # Calculate Helga's regular articles
    regular_articles = WRITING_RATE * REGULAR_HOURS

    # Calculate Helga's articles from Thursday
    thursday_hours = 4 + 2 # 4 regular hours plus 2 extra hours
    thursday_articles = WRITING_RATE * thursday_hours

    # Calculate Helga's articles from Friday
    friday_hours = 4 + 3 # 4 regular hours plus 3 extra hours
    friday_articles = WRITING_RATE * friday_hours

    # Calculate Helga's total articles for the week
    total_articles = regular_articles + thursday_articles + friday_articles

    # Display Helga's total articles for the week
    result = total_articles
    return result

print(solution())