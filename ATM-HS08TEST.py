def atm():
    txn_charges = 0.50
    withdraw_amt, initial_amount = map(float, input().split())
    if withdraw_amt % 5 == 0 and withdraw_amt < initial_amount:
        initial_amount = "{0:.2f}".format(initial_amount)
        remaining = "{0:.2f}".format(float(initial_amount) - txn_charges - float(withdraw_amt))
        print(remaining)
    elif withdraw_amt > initial_amount:
        print("{0:.2f}".format(initial_amount))
    else:
        print("{0:.2f}".format(initial_amount))

atm()