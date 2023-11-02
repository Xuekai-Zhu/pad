def solution():
    # Calculate the number of chocolate cookies Andy had initially
    cookies = 3 + 5 + sum([2 * i + 1 for i in range(8)])  # Andy ate 3 cookies and gave away 5, then each player took an odd number of cookies starting with 1 and increasing by 2 for each subsequent player
    result = cookies
    return result

print(solution())