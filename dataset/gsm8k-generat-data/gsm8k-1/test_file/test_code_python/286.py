def solution():
    """Ali is a superstar counter. He has won 22 medals for counting super fast. His friend Izzy is also a really good counter and has 5 less medals than Ali. Together they have 10 times less medals than have been given out for counting. How many medals have been given out for counting?"""
    ali_medals = 22
    izzy_medals = ali_medals - 5
    total_medals = (ali_medals + izzy_medals) * 10
    result = total_medals
    return result

print(solution())