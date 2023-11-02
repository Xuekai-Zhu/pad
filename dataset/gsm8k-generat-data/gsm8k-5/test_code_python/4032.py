def solution():
    total_scientists = 70  # There are 70 scientists in total
    europe_scientists = total_scientists / 2  # Half of the scientists are from Europe
    canada_scientists = total_scientists / 5  # One-fifth of the scientists are from Canada
    USA_scientists = total_scientists - europe_scientists - canada_scientists  # The rest of the scientists are from the USA
    result = USA_scientists
    return result

print(solution())