import argparse
import math

parser = argparse.ArgumentParser(description="This program is Loan calculator. It has capacity to compute \
differentiated or annuity payments")

parser.add_argument("--type")
# , choices=["annuity", "diff"])

parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest")

args = parser.parse_args()

parameters = [args.type, args.principal, args.periods, args.interest]

if args.type == "annuity":
    parameters.append(args.payment)
print(args)

if args.type != "diff":
    if args.type != "annuity":
        print("Incorrect parameters")


def diff_payment(principal, periods, interest):
    m = 1
    i = float(interest) / 12 / 100
    sum_ = 0
    while m <= periods:
        diff_p = principal / periods + i * (principal - principal * (m - 1) / periods)
        d = math.ceil(diff_p)
        print(f'Month {m}: payment is {d}')
        m += 1
        sum_ += d
    print(f'Overpayment {sum_ - principal}')

    if args.type == "diff":
        if args.payment in parameters:
            print("Incorrect parameters")
        elif args.principal and args.periods and args.interest not in parameters:
            print("Incorrect parameters")
        else:
            diff_payment(args.principal, args.periods, args.interest)
