def solution():
    # Initial email count
    email_count = 0

    # Delete 50 emails and receive 15 new emails
    email_count += -50 + 15

    # Delete 20 more emails and receive 5 new emails
    email_count += -20 + 5

    # Add 10 new emails
    email_count += 10

    result = email_count
    return result

print(solution())