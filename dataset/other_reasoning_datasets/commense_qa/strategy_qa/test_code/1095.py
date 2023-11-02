def solution():
    egot_awards = ["Emmy", "Grammy", "Oscar", "Tony"]
    christopher_walken_awards = ["Oscar", "Tony", "Emmy"]
    egot_progress = [award for award in egot_awards if award not in christopher_walken_awards]
    if len(egot_progress) == 1: # only missing one award
        result = f"Yes, Christopher Walken is close to achieving EGOT status. He has won an {christopher_walken_awards[0]} and been nominated for a {egot_progress[0]}."
    else:
        result = "No, Christopher Walken is not close to achieving EGOT status."
    return result

print(solution())