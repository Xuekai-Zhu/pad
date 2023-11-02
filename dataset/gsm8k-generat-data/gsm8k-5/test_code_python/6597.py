def solution():
    jacob_fish = 8  # Jacob caught 8 fish at the beginning
    alex_fish = jacob_fish * 7  # Alex caught 7 times as many fish as Jacob

    # Adjust Alex's catch due to losing 23 fish
    alex_fish -= 23

    # Calculate the number of fish Jacob needs to catch to beat Alex
    difference = alex_fish - jacob_fish - 1

    result = difference
    return result

print(solution())