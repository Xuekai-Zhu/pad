def solution():
    """Mark had 10 pieces of fruit to eat in school this week. On Friday, he decided to keep 2 pieces of fruit for next week. He then brings the remaining 3 pieces of fruit to school for the day. How many pieces of fruit did Mark eat in the first four days of the week?"""
    # Define the total number of fruit Mark had
    total_fruit = 10

    # Calculate the number of fruit Mark kept for next week
    kept_fruit = 2

    # Calculate the number of fruit Mark brought to school on Friday
    friday_fruit = 3

    # Calculate the number of fruit Mark had in the first four days
    first_four_days_fruit = total_fruit - kept_fruit - friday_fruit

    # Display the number of fruit Mark had in the first four days
    result = first_four_days_fruit
    return result

print(solution())