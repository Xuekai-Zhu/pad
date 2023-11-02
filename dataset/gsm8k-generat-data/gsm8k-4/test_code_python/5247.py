def solution():
    """Grant spends $200.00 a year to have the newspaper delivered daily to his house. Juanita buys the newspaper daily. Monday through Saturday, she spends $0.50 and on Sunday she spends $2.00. How much more money does Juanita spend buying the newspaper yearly than Grant?"""
    # Calculate how much Juanita spends on the newspaper from Monday to Saturday
    daily_expenditure = 0.5
    weekly_expenditure = daily_expenditure * 6

    # Calculate how much Juanita spends on the newspaper on Sunday
    sunday_expenditure = 2.0

    # Calculate how much Juanita spends on the newspaper in a year
    yearly_expenditure = weekly_expenditure * 52 + sunday_expenditure * 52

    # Calculate the difference between Juanita's and Grant's expenses
    difference = yearly_expenditure - 200.0

    # Round the result to two decimal points
    result = round(difference, 2)

    return result

print(solution())