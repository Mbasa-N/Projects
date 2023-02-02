print("SA Tax Calculator")
salary = int(input("Enter your salary per annum: "))

if salary <= 205900:
    tax = salary * 0.18
    print(f"Your payable tax amount is R{tax}")

elif salary >= 205901 and salary <= 321600:
    tax_base = 37062
    tax_diff = salary - 205900
    tax = tax_diff * 0.26
    payable_tax = tax_base + tax
    print(f"Your payable tax amount is R{payable_tax}")

elif salary >= 321601 and salary <= 445100:
    tax_base = 67144
    tax_diff = salary - 321600
    tax = tax_diff * 0.31
    payable_tax = tax_base + tax
    print(f"Your payable tax amount is R{payable_tax}")

elif salary >= 445101 and salary <= 584200:
    tax_base = 105429
    tax_diff = salary - 445100
    tax = tax_diff * 0.36
    payable_tax = tax_base + tax
    print(f"Your payable tax amount is R{payable_tax}")

elif salary >= 584201 and salary <= 744800:
    tax_base = 155505
    tax_diff = salary - 584200
    tax = tax_diff * 0.39
    payable_tax = tax_base + tax
    print(f"Your payable tax amount is R{payable_tax}")

elif salary >= 744801 and salary <= 1577300:
    tax_base = 218139
    tax_diff = salary - 744800
    tax = tax_diff * 0.41
    payable_tax = tax_base + tax
    print(f"Your payable amount is {payable_tax}")

elif salary >= 1577301:
    tax_base = 559464
    tax_diff = salary - 1577300
    tax = tax_diff * 0.45
    payable_tax = tax_base + tax
    print(f"Your payable amount is R{payable_tax}")