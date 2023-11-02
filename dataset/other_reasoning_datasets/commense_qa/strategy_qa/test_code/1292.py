def solution():
    call_waiting_invented_year = 1970
    alexander_graham_bell_phone_year = 1876
    if call_waiting_invented_year > alexander_graham_bell_phone_year:
        result = "no"
    else:
        result = "N/A"
    return result

#Explanation: Call waiting wasn't invented or available during the time Alexander Graham Bell's phone was used. Therefore, the result is "no". However, since call waiting didn't exist during Alexander Graham Bell's time, the result is "N/A" for the question of whether his phone had call waiting.

print(solution())