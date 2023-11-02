def solution():
    # Calculate the number of fish Chris catches per trip
    chris_fish_per_trip = 400 / (3/5)  # Brian catches 2/5 times fewer fish than Chris per trip

    # Calculate the total number of fish caught by Chris
    total_chris_fish = chris_fish_per_trip * 10  # Chris went fishing 10 times

    # Calculate the total number of fish caught by Brian
    total_brian_fish = 400 * 20  # Brian goes fishing twice as often as Chris

    # Calculate the total number of fish caught by both Chris and Brian
    total_fish = total_chris_fish + total_brian_fish
    result = total_fish
    return result

print(solution())