def solution():
    """Jasmine gets off of work at 4:00 pm. After that, it will take her 30 minutes to commute home, 30 minutes to grocery shop, 10 minutes to pick up the dry cleaning, 20 minutes to pick up the dog from the groomers and 90 minutes to cook dinner when she returns home. What time will she eat dinner?"""
    commute_time = 30 # minutes
    grocery_time = 30 # minutes
    dry_cleaning_time = 10 # minutes
    groomer_time = 20 # minutes
    cooking_time = 90 # minutes
    total_time = commute_time + grocery_time + dry_cleaning_time + groomer_time + cooking_time # minutes
    dinner_time = 4*60 + total_time # convert 4:00 pm to minutes and add total time
    hours = dinner_time // 60 # integer division gives hours
    minutes = dinner_time % 60 # modulo gives minutes
    return f"{hours}:{minutes:02}" # format as hh:mm string

print(solution())