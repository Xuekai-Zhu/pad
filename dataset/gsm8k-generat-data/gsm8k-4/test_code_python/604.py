def solution():
    """Santana has 7 brothers. 3 of them have birthdays in March, 1 of them has a birthday in October, 1 has a birthday in November, and another 2 of them were born in December. If Santana always buys each of her brothers a birthday present and a Christmas present, how many more presents does she have to buy in the second half of the year than the first half of the year?"""
    # Define the number of brothers with birthdays in each month
    march_birthdays = 3
    october_birthdays = 1
    november_birthdays = 1
    december_birthdays = 2

    # Define the total number of brothers
    total_brothers = 7

    # Calculate the number of presents to buy in the first half of the year
    first_half_presents = (march_birthdays + october_birthdays + november_birthdays) * 2

    # Calculate the number of presents to buy in the second half of the year
    second_half_presents = (total_brothers - (march_birthdays + october_birthdays + november_birthdays)) * 2

    # Calculate the difference between the two
    difference = second_half_presents - first_half_presents

    # Display the result
    result = difference
    return result

print(solution())