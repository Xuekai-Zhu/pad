def solution():
    tickle_me_elmo_popularity_year = 1996
    snoop_dogg_age_in_popularity_year = 25
    # determine the birth year based on Snoop Dogg's age and the year of Tickle Me Elmo's popularity
    snoop_dogg_birth_year = tickle_me_elmo_popularity_year - snoop_dogg_age_in_popularity_year
    # determine if Snoop Dogg was an adult at the time of Tickle Me Elmo's popularity
    if snoop_dogg_birth_year <= 18:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())