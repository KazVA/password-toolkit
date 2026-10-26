
import argparse
import math
import secrets
import string


def generate(length):
    if length < 1:
        raise ValueError("Length must be at least 1")

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def entropy(password):
    pool = (
        26 * any(c.islower() for c in password)
        + 26 * any(c.isupper() for c in password)
        + 10 * any(c.isdigit() for c in password)
        + 32 * any(c in string.punctuation for c in password)
    )

    return len(password) * math.log2(pool) if pool else 0


def rate(bits):
    if bits < 40:
        return "Weak"
    elif bits < 60:
        return "OK"
    elif bits < 80:
        return "Strong"
    return "Excellent"


parser = argparse.ArgumentParser(
    description="Password generator and strength checker"
)

sub = parser.add_subparsers(dest="cmd", required=True)

gen = sub.add_parser("gen", help="Generate a random password")
gen.add_argument("-l", "--length", type=int, default=16)

check = sub.add_parser("check", help="Estimate password entropy")
check.add_argument("password")

args = parser.parse_args()

if args.cmd == "gen":
    if args.length < 1:
        parser.error("Password length must be at least 1")

    password = generate(args.length)
    print(f"{password} ({rate(entropy(password))})")

else:
    bits = entropy(args.password)
    print(f"{bits:.0f} bits of estimated entropy: {rate(bits)}")
