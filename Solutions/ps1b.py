# Salário anual
annual_salary = float(input("Enter your annual salary: "))

# Percentual do salário a economizar por mês
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

# Custo do meu sonho
total_cost = float(input("Enter the cost of your dream home: "))

# Aumento de salário a cada 6 meses
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

monthly_salary = annual_salary/12

# Dinheiro economizado
current_savings = 0

# Rendimento anual
r = 0.04

# Entrada
portion_down_payment = 0.25 * total_cost

months = 0



while(current_savings < portion_down_payment):
    current_savings = current_savings + (current_savings * r / 12) + (
            portion_saved * monthly_salary)
    months += 1

    if months % 6 == 0
        monthly_salary = monthly_salary + monthly_salary * semi_annual_raise
    
print("Number of months: ", months)