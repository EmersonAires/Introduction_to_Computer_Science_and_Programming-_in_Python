# Salário anual
annual_salary = float(input("Enter your annual salary: "))

# Percentual do salário a economizar por mês
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

# Custo do meu sonho
total_cost = float(input("Enter the cost of your dream home: "))

monthly_salary = annual_salary/12

# Dinheiro economizado
current_savings = 0

# Rendimento anual
r = 0.04

# Entrada
portion_down_payment = 0.25 * total_cost

#Total = [Juros compostos do principal] + [Valor futuro de uma série]
#Total = [P(1 + r/n)^(nt)] + [PMT x (((1 + r/n)^(nt)-1)/(r/n))]

months = 0

while(current_savings < portion_down_payment):
    current_savings = current_savings + (current_savings * r / 12) + (
            portion_saved * monthly_salary)
    months += 1
    
print("Number of months: ", months)