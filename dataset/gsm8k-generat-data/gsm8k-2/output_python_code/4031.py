def solution():
    """Paul is working at a university. He is part of a big project, which involves 70 scientists in total. Half of them are from Europe and one-fifth are from Canada. The rest are from the USA. How many scientists in this project are from the USA?"""
    total_scientists = 70
    europe_scientists = total_scientists / 2
    canada_scientists = total_scientists / 5
    usa_scientists = total_scientists - europe_scientists - canada_scientists
    result = usa_scientists
    return result

print(solution())