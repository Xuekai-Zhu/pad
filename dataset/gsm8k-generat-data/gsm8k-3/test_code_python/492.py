def solution():
    """There are 40 Judges in the state of Rhode Island.  10 percent of Judges are under 30 years old.  60 percent of Judges are 30-50 years old.  The rest of the Judges are over 50 years old.  How many Judges are over 50 years old?"""
    # Define the total number of judges
    total_judges = 40

    # Calculate the number of judges under 30 years old
    under30_judges = round(total_judges * 0.1)

    # Calculate the number of judges between 30 and 50 years old
    thirty_fifty_judges = round(total_judges * 0.6)

    # Calculate the remaining number of judges over 50 years old
    over50_judges = total_judges - under30_judges - thirty_fifty_judges

    # Display the number of judges over 50 years old
    result = over50_judges
    return result

print(solution())