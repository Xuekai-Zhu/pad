def solution():
    """An archaeologist discovered three dig sites from different periods in one area. The archaeologist dated the first dig site as 352 years more recent than the second dig site. The third dig site was dated 3700 years older than the first dig site. The fourth dig site was twice as old as the third dig site. The archaeologist studied the fourth dig site’s relics and gave the site a date of 8400 BC. What year did the archaeologist date the second dig site?"""
    # Define the date of the fourth dig site
    fourth_date = -8400

    # Calculate the date of the third dig site
    third_date = fourth_date / 2

    # Calculate the date of the first dig site
    first_date = third_date - 3700

    # Calculate the date of the second dig site
    second_date = first_date - 352

    # Display the date of the second dig site
    result = 2020 - second_date
    return result

print(solution())