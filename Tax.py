def get_inputs():
    basic_salary = float(input("Enter Basic Salary: ₹"))
    hra_percent = float(input("Enter HRA %: "))
    da_percent = float(input("Enter DA %: "))
    tax_percent = float(input("Enter Tax %: "))
    return basic_salary, hra_percent, da_percent, tax_percent

def calculate_salary(basic_salary, hra_percent, da_percent, tax_percent):
    hra = (hra_percent / 100) * basic_salary
    da = (da_percent / 100) * basic_salary

    gross_salary = basic_salary + hra + da
    tax = (tax_percent / 100) * gross_salary
    net_salary = gross_salary - tax

    return gross_salary, tax, net_salary

def display_result(gross_salary, tax, net_salary):
    print("\n Salary Details ")
    print(f"Gross Salary: ₹{gross_salary:.2f}")
    print(f"Tax: ₹{tax:.2f}")
    print(f"Net Salary: ₹{net_salary:.2f}")

def main():
    print(" Employee Salary Calculator ")
    basic_salary, hra_percent, da_percent, tax_percent = get_inputs()
    gross_salary, tax, net_salary = calculate_salary(basic_salary, hra_percent, da_percent, tax_percent)
    display_result(gross_salary, tax, net_salary)

main()