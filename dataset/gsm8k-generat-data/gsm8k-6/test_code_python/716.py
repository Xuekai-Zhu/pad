def solution():
    # Convert Margaret's money from dollars to cents
    margaret_money = (3/4) * 100  

    # Convert Guy's money from quarters and dimes to cents
    guy_money = 2 * 25 + 10  

    # Convert Bill's money from dimes to cents
    bill_money = 6 * 10  

    # Add up the total money in cents
    total_money = 70 + margaret_money + guy_money + bill_money
    result = total_money
    return result

print(solution())