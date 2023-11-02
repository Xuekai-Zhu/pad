def solution():
    # Calculate the number of pieces of fruit Mark had on Friday
    fruits_on_friday = 2

    # Calculate the number of pieces of fruit Mark brought to school on Friday
    fruits_to_school_on_friday = 3

    # Calculate the total number of fruits Mark had before Friday
    total_fruits = 10 - fruits_on_friday

    # Calculate the total number of fruits Mark ate in the first four days of the week
    fruits_eaten = total_fruits - fruits_to_school_on_friday

    result = fruits_eaten
    return result

print(solution())