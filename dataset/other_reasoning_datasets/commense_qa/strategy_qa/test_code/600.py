def solution():
    wodehouse_birthyear = 1881
    internet_conception_year = 1965
    if wodehouse_birthyear < internet_conception_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())