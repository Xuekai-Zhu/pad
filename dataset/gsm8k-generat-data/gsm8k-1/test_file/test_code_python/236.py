def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_last = len('Grey')
    bobbie_last = jamie_last * 2 + 2
    samantha_last = bobbie_last - 3
    result = samantha_last
    return result

def solution():
    """James has 6 more candies than Robert. John has twice as many candies as Robert. If John has 54 candies, how many more candies does John have than James?"""
    john_candies = 54
    robert_candies = john_candies / 2
    james_candies = robert_candies + 6
    difference = john_candies - james_candies
    result = difference
    return result

print(solution())