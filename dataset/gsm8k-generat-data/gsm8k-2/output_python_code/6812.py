def solution():
    """The tallest building in the world is 100 feet tall. If the second tallest is half that tall, and the third tallest is half as tall as the second, and the fourth is one-fifth as tall as the third, how tall are all 4 buildings put together?"""
    tallest = 100
    second = tallest / 2
    third = second / 2
    fourth = third / 5
    total = tallest + second + third + fourth
    result = total
    return result

print(solution())