def solution():
    ed_snowden_twitter = True
    ed_snowden_tv_commentary = True
    ed_snowden_residence = "Russia" # Retrieved from Wikipedia
    if ed_snowden_residence != "United States" and (ed_snowden_twitter or ed_snowden_tv_commentary):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())