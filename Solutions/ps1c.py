# Salário anual
annual_salary = float(input("Enter your annual salary: "))

# Custo do meu sonho
total_cost = 1000000

# Aumento de salário a cada 6 meses
semi_annual_raise = 0.07

# Dinheiro economizado
current_savings = 0

# Rendimento anual
r = 0.04

# Entrada
portion_down_payment = 0.25 * total_cost
epsilon = 100

max_portion_saved = 10000
min_portion_saved = 0
possible_to_pay_in_three_years = True

##################################################################################################

def calc_current_savings(portion_saved): 
     
    '''Calcula o valor poupado em 36 meses'''

    months = 1
    global current_savings
    current_savings = 0
    monthly_salary = (annual_salary / 12)
    
    semi_annual_raise = 0.07

    while(months <= 36):

        current_savings = current_savings + (current_savings * (r / 12)) + (
            portion_saved * monthly_salary)

        if months % 6 == 0:
            monthly_salary = monthly_salary + (monthly_salary * semi_annual_raise)
        
        months += 1

    return current_savings

#####################################################################################

# Verifica se a diferença entre o valor da entrada e do valor salvo
# está dentro do epsilon definido

interations = 0

while abs(portion_down_payment - current_savings) > epsilon:

    portion_saved_mide = (max_portion_saved + min_portion_saved) // 2
    portion_saved_mide_rate = portion_saved_mide / 10000

    if calc_current_savings(portion_saved_mide_rate) > portion_down_payment:
        max_portion_saved = portion_saved_mide - 1
    else:
        min_portion_saved = portion_saved_mide + 1

    if min_portion_saved >= max_portion_saved:
        print("it is not possible to pay the down payment in three years")
        possible_to_pay_in_three_years = False
        break
    
    interations += 1

if possible_to_pay_in_three_years:
    print("Best savings rate: " + str(portion_saved_mide_rate), "Value saving: " + str(current_savings))
    print("Steps in bisection search: " + str(interations))



