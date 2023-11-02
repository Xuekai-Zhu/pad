def solution():
    """Santana has 7 brothers. 3 of them have birthdays in March, 1 of them has a birthday in October, 1 has a birthday in November, and another 2 of them were born in December. If Santana always buys each of her brothers a birthday present and a Christmas present, how many more presents does she have to buy in the second half of the year than the first half of the year?"""
    # Define the number of brothers with birthdays in each month
    march_birthdays = 3
    october_birthdays = 1
    november_birthdays = 1
    december_birthdays = 2

    # Calculate the total number of brothers with birthdays in the first half of the year
    first_half_birthdays = march_birthdays

    # Calculate the total number of brothers with birthdays in the second half of the year
    second_half_birthdays = october_birthdays + november_birthdays + december_birthdays

    # Calculate the total number of presents Santana needs to buy in the first half of the year
    first_half_presents = 2 * first_half_birthdays

    # Calculate the total number of presents Santana needs to buy in the second half of the year
    second_half_presents = 2 * second_half_birthdays

    # Calculate the difference in the total number of presents Santana needs to buy
    difference = second_half_presents - first_half_presents

    # Display the difference in the total number of presents Santana needs to buy
    result = difference
    return result

print(solution())