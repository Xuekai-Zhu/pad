def solution():
    # Calculate the amount of money from selling red stamps
    money_red_stamps = 30 * 0.5  # each red stamp is sold for 50 cents

    # Calculate the amount of money from selling white stamps
    money_white_stamps = 80 * 0.2  # each white stamp is sold for 20 cents

    # Calculate the difference in the amount of money they make in dollars
    difference = (money_white_stamps - money_red_stamps) / 100  # divide by 100 to convert cents to dollars
    result = round(difference, 2)  # round to 2 decimal places
    return result

print(solution())