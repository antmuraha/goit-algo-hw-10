from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, value

# Initialize the problem
problem = LpProblem("Maximize_Production", LpMaximize)

# Define the decision variables
lemonade = LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Define the objective function
problem += lemonade + fruit_juice, "Total_Production"

# Define the constraints
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solve the problem
problem.solve()

# Output the results
print("Status:", LpStatus[problem.status])
print("Lemonade to produce:", lemonade.varValue)
print("Fruit Juice to produce:", fruit_juice.varValue)
print("Total Production:", (lemonade.varValue + fruit_juice.varValue))
