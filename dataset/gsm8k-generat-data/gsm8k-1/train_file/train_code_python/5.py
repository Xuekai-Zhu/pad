def solution():
    """Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?"""
    yellow_plants = 10
    purple_plants = yellow_plants * 1.8
    total_plants = yellow_plants + purple_plants
    green_plants = 0.25 * (yellow_plants + purple_plants)
    total_flowers = yellow_plants + purple_plants + green_plants
    result = total_flowers
    return result

print(solution())