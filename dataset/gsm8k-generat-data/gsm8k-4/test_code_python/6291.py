def solution():
    """Andy had a platter of chocolate cookies. He ate 3 of them then gave his little brother 5 because he was behaving. He then handed the platter to his basketball team of eight members. The first player to arrive took 1, the second player to arrive took 3, the third player took 5, and so on. When the last player took his share, the platter was empty. How many chocolate cookies did Andy have from start with?"""
    # Define the initial number of cookies
    initial_cookies = None

    # Define the number of cookies that Andy ate
    andy_ate = 3

    # Define the number of cookies that Andy gave to his brother
    andy_gave = 5

    # Define the number of players on the basketball team
    players = 8

    # Define the sum of the arithmetic series of odd numbers from 1 to 2n - 1
    def odd_series_sum(n):
        return n**2

    # Calculate the number of cookies that the basketball team took
    team_cookies = odd_series_sum(players) - odd_series_sum(players//2)

    # Calculate the initial number of cookies
    initial_cookies = andy_ate + andy_gave + team_cookies

    result = initial_cookies
    return result

print(solution())