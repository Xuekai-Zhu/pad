def solution():
    """Mr. Roper cuts his lawn 15 days a month beginning in April and ending in September.  From October to the end of March he cuts his lawn three times a month.  What is the average number of times that Mr. Roper cuts his yard per month?"""
    # Calculate the number of months from April to September
    months1 = 6

    # Calculate the number of times Mr. Roper cuts his lawn from April to September
    cuts1 = 15 * months1

    # Calculate the number of months from October to March
    months2 = 6

    # Calculate the number of times Mr. Roper cuts his lawn from October to March
    cuts2 = 3 * months2

    # Calculate the total number of times Mr. Roper cuts his lawn in a year
    total_cuts = cuts1 + cuts2

    # Calculate the average number of times Mr. Roper cuts his lawn per month
    avg_cuts = total_cuts / 12

    # Display the average number of times Mr. Roper cuts his lawn per month
    result = avg_cuts
    return result

print(solution())