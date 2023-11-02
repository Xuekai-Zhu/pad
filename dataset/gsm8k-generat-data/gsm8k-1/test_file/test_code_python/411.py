def solution():
    """While Joanne is gathering apples from her family’s orchard, her sister comes outside to help her. Joanne gathers 30 apples from the tallest trees, half this amount from the shortest trees, and more apples from the average trees. Compared with Joanne, her sister gathers twice as many apples from the tallest trees and 3 times as many apples from the shortest trees. She doesn't take any from the average trees. If the sisters have gathered a combined total of 500 apples, how many apples did Joanne gather from the average trees?"""
    joanne_tallest = 30
    joanne_shortest = joanne_tallest / 2
    sister_tallest = joanne_tallest * 2
    sister_shortest = joanne_shortest * 3
    sister_average = 0
    total_apples = 500
    joanne_average = (total_apples - joanne_tallest - joanne_shortest - sister_tallest - sister_shortest) / 2
    result = joanne_average
    return result

print(solution())