def solution():
    """Elsa gets 500 MB of cell phone data each month. If she spends 300 MB watching Youtube and 2/5 of what's left on Facebook, how many MB of data does she have left?"""
    # Define the amount of cell phone data Elsa gets each month
    MONTHLY_DATA = 500

    # Calculate how much data Elsa has left after watching Youtube
    data_left = MONTHLY_DATA - 300

    # Calculate how much data Elsa spends on Facebook
    facebook_data = data_left * (2/5)

    # Calculate how much data Elsa has left after watching Youtube and using Facebook
    data_left -= facebook_data

    # Display how much data Elsa has left
    result = data_left
    return result

print(solution())