import argparse
import math

parser = argparse.ArgumentParser(description="This program is Loan calculator. It has capacity to compute \
differentiated or annuity payments")

parser.add_argument("--type")
# , choices=["annuity", "diff"])

parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

parameters = [args.type, args.principal, args.periods, args.interest]

if args.type == "annuity":
    parameters.append(args.payment)
# print(args)

if args.type != "diff":
    if args.type != "annuity":
        print("Incorrect parameters")

    else:
        def annuity_payment(principal, periods, interest):
            i = interest / 12 / 100
            annuity_pay = math.ceil(principal * i * math.pow((1 + i), periods) / (math.pow((1 + i), periods) - 1))
            print(f'Your monthly payment = {annuity_pay}!')
            print(f'Overpayment = {annuity_pay * periods - principal}')


        def annuity_principal(periods, interest, payment):
            i = interest / 12 / 100
            annuity_pr = math.floor(payment / (i * math.pow((1 + i), periods) / (math.pow((1 + i), periods) - 1)))
            print(f'Your loan principal = {annuity_pr}!')
            print(f'Overpayment = {periods * payment - annuity_pr}')


        def annuity_periods(principal, interest, payment):
            i = interest / 100 / 12
            annuity_per = math.ceil(math.log((payment / (payment - i * principal)), (1 + i)))
            a = annuity_per / 12
            b = annuity_per % 12
            c = annuity_per // 12
            if a < 1:
                print(f'It will take {annuity_per} month{"" if annuity_per == 1 else "s"} to repay this loan!')
            elif b == 0:
                print(f'It will take {c} year{"" if c == 1 else "s"} to repay this loan!')
            else:
                print(f'It will take {c} year{"" if c == 1 else "s"} '
                      f'and {a - c} month{"" if b == 1 else "s"} to repay this loan!')
            print(f'Overpayment = {annuity_per * payment - principal}')


        if args.payment is None:
            annuity_payment(args.principal, args.periods, args.interest)
        elif args.principal is None:
            annuity_principal(args.periods, args.interest, args.payment)
        elif args.periods is None:
            annuity_periods(args.principal, args.interest, args.payment)
        else:
            print("Incorrect parameters")


else:
    def diff_payment(principal, periods, interest):
        m = 1
        i = interest / 12 / 100
        sum_ = 0
        while m <= periods:
            diff_p = principal / periods + i * (principal - principal * (m - 1) / periods)
            d = math.ceil(diff_p)
            print(f'Month {m}: payment is {d}')
            m += 1
            sum_ += d
        print(f'Overpayment = {sum_ - principal}')

    if args.payment is not None:
        print("Incorrect parameters")
    elif args.principal < 0 or args.periods < 0 or args.interest < 0:
        print("Incorrect parameters")
    else:
        diff_payment(args.principal, args.periods, args.interest)


# diff and annuity work
