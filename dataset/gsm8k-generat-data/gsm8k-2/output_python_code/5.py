def solution():
    """Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?"""
    yellow_flowers = 10
    purple_flowers = yellow_flowers * 1.8
    total_flowers = yellow_flowers + purple_flowers
    green_flowers = total_flowers * 0.25
    total_flowers += green_flowers
    result = total_flowers
    return result

print(solution())