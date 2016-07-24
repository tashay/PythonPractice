import sys
import re

balance = 0

for line in sys.stdin:
    prog = re.compile("([WD]) (\\d+)\n")
    match = prog.fullmatch(line)
    if match:
        activity = match.group(1)
        amount = int(match.group(2))
        if activity == "W":
            balance -= amount
        elif activity == "D":
            balance += amount
    else:
        print('Did not match.')

print("Balance:" , balance)
