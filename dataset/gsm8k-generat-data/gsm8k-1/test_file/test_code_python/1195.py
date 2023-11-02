def solution():
    """Fred was preparing for a party to be held in four days. So, he made 24 gallons of root beer on the first day and put them in the refrigerator cooler. But later that evening, his children discovered the delicious nectar and robbed the cooler, drinking 4 of those gallons of root beer. On the second day, his wife Barbie also discovered the root beer and accidentally spilled 7 gallons. On the third day, Fred's friend Ronnie visited Fred's house and helped himself to the root beer, further reducing the amount remaining by 5 gallons. On the fourth day, 3 people showed up for the party. If Fred and the others shared the remaining root beer equally, how much was available for each to drink during the party?"""
    initial_root_beer = 24
    root_beer_drunk_day1 = 4
    root_beer_spilled_day2 = 7
    root_beer_drunk_day3 = 5
    total_root_beer = initial_root_beer - root_beer_drunk_day1 - root_beer_spilled_day2 - root_beer_drunk_day3
    people_at_party = 4
    root_beer_per_person = total_root_beer // people_at_party
    result = root_beer_per_person
    return result

print(solution())