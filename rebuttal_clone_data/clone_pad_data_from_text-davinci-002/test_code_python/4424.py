def solution():
    total_guests = 200
    percent_women = 40
    women = total_guests * (percent_women / 100)
    percent_wearing_ears = 80
    women_wearing_ears = women * (percent_wearing_ears / 100)
    percent_men_wearing_ears = 60
    men_wearing_ears = total_guests * (1 - (percent_women / 100)) * (percent_men_wearing_ears / 100)
    total_wearing_ears = women_wearing_ears + men_wearing_ears
    result = total_wearing_ears
    return result

print(solution())