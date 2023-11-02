def solution():
    people = 24
    sandwiches_per_person = 2
    total_sandwiches = people * sandwiches_per_person
    croissants_per_sandwich = 1
    total_croissants = total_sandwiches * croissants_per_sandwich
    price_per_dozen_croissants = 8
    total_price = total_croissants / 12 * price_per_dozen_croissants
    result = total_price
    return result

print(solution())