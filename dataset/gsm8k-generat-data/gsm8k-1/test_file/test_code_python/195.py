def solution():
    """Mark is a copy-editor. He edits an equal number of sentences each week for two different publishers, who each pay him a different rate per sentence. Publisher B pays Mark twice what Publisher A pays. Mark edits a total number of 1000 sentences each week, and Publisher A pays him 5 cents per sentence. How much does Mark make in a week, in cents?"""
    total_sentences = 1000
    rate_a = 5
    rate_b = rate_a * 2
    sentences_per_publisher = total_sentences / 2
    payment_a = sentences_per_publisher * rate_a
    payment_b = sentences_per_publisher * rate_b
    total_payment = payment_a + payment_b
    result = total_payment
    return result

print(solution())