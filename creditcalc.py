import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
args = parser.parse_args()


def check_parameters():
    if args.type not in ["diff", "annuity"]:
        print(1)
        print("Incorrect parameters")
        exit()

    if args.type == "diff" and args.payment is not None:
        print(2)
        print("Incorrect parameters")
        exit()

    if args.principal is not None:
        if args.principal < 0:
            print(3)
            print("Incorrect parameters")
            exit()

    if args.periods is not None:
        if args.periods < 0:
            print(4)
            print("Incorrect parameters")
            exit()

    if args.interest is None:
        print(5)
        print("Incorrect parameters")
        exit()

    if args.interest < 0:
        print(6)
        print("Incorrect parameters")
        exit()

    if args.payment is not None:
        if args.payment < 0:
            print(7)
            print("Incorrect parameters")
            exit()


def choice():
    if args.type == "diff":
        differentiate(args.principal, args.periods, calc_nominal(args.interest))
    elif args.periods is None:
        no_payments(args.principal, args.payment, calc_nominal(args.interest))
    elif args.principal is None:
        loan_principal(args.payment, calc_nominal(args.interest), args.periods)
    elif args.payment is None:
        annuity_calc(args.principal, calc_nominal(args.interest), args.periods)


def annuity_calc(princ, i, per):
    a = i * pow(1 + i, per)
    b = pow(1 + i, per) - 1
    c = princ * a / b
    print("Your annuity payment =", math.ceil(c), "!")
    print("Overpayment = {}".format(math.ceil((per * math.ceil(c) - princ))))


def loan_principal(pay, i, per):
    a = i * pow(1 + i, per)
    b = pow(1 + i, per) - 1
    c = pay * b / a
    print("Your loan principal =", math.ceil(math.floor(c)), "!")
    print("Overpayment = {}".format(math.ceil(per * pay - c)))


def no_payments(princ, pay, i):
    n = math.log(pay/(pay - i * princ), 1 + i)
    months = math.ceil(n)
    if months // 12 == 0:
        print("It will take", months % 12, "months to repay this loan!")
    elif months % 12 == 0:
        print("It will take", months // 12, "years to repay this loan!")
    else:
        print("It will take", months // 12, "years and", months % 12, "months to repay this loan!")
    print("Overpayment = {}".format(math.ceil((months * pay) - princ)))


def differentiate(princ, per, i):
    overpayment = 0
    for month in range(per):
        diff_annuity = math.ceil((princ / per) + i * (princ - (princ * month) / per))
        print("Month {}: payment is {}".format(month + 1, diff_annuity))
        overpayment += diff_annuity
    print()
    print("Overpayment = {}".format(math.ceil(overpayment - princ)))


def calc_nominal(interest_rate):
    return (interest_rate / 100) / 12


if __name__ == '__main__':
    check_parameters()
    choice()



