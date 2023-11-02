def solution():
    jackson_5_members = 5
    isley_brothers_members = 4
    jackson_5_albums_sold = 100_000_000
    isley_brothers_albums_sold = 18_000_000
    if jackson_5_members > isley_brothers_members and jackson_5_albums_sold > isley_brothers_albums_sold:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())