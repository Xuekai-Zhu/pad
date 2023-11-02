def solution():
    # Define the dates of Stone Cold Steve Austin's debut and retirement
    debut_date = "September 30, 1989"
    retirement_date = "March 30, 2003"
    # Convert the dates into datetime objects
    debut = datetime.datetime.strptime(debut_date, "%B %d, %Y")
    retirement = datetime.datetime.strptime(retirement_date, "%B %d, %Y")
    # Check if Stone Cold Steve Austin wrestled in three different centuries
    if debut.year < 2001 and retirement.year >= 2001:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())