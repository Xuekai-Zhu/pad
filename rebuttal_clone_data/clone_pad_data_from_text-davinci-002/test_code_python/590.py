def solution():
    total_bars = 100
    milk_chocolate_bars = 25
    dark_chocolate_bars = 25
    milk_chocolate_almond_bars = 25
    white_chocolate_bars = 25
    milk_chocolate_percentage = milk_chocolate_bars / total_bars * 100
    dark_chocolate_percentage = dark_chocolate_bars / total_bars * 100
    milk_chocolate_almond_percentage = milk_chocolate_almond_bars / total_bars * 100
    white_chocolate_percentage = white_chocolate_bars / total_bars * 100
    result = [milk_chocolate_percentage, dark_chocolate_percentage, milk_chocolate_almond_percentage, white_chocolate_percentage]

    return result

print(solution())