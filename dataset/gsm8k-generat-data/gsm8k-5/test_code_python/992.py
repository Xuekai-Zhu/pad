def solution():
    bananas = 20  # Hannah is using 20 bananas
    bananas_per_cup = 4  # It takes 4 bananas to make one cup of banana mush
    cups_of_mush = bananas / bananas_per_cup  # Calculate the number of cups of banana mush Hannah will use
    cups_of_flour = 3 * cups_of_mush  # Hannah needs 3 cups of flour for every cup of banana mush
    result = cups_of_flour
    return result

print(solution())