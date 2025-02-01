# Production Optimization

The company produces two types of beverages: "Lemonade" and "Fruit Juice." The production of these beverages requires different ingredients and a limited amount of equipment. The objective is to maximize production while considering resource constraints.

## Task Conditions:
- Lemonade is made from "Water," "Sugar," and "Lemon Juice."
- Fruit Juice is made from "Fruit Puree" and "Water."

- Resource Constraints:
    - 100 units of "Water"
    - 50 units of "Sugar"
    - 30 units of "Lemon Juice"
    - 40 units of "Fruit Puree"

## Production Requirements:

- Producing one unit of "Lemonade" requires:
    - 2 units of "Water"
    - 1 unit of "Sugar"
    - 1 unit of "Lemon Juice"

- Producing one unit of "Fruit Juice" requires:
    - 2 units of "Fruit Puree"
    - 1 unit of "Water"

Using PuLP, create a model that determines how many units of "Lemonade" and "Fruit Juice" should be produced to maximize the total number of products while adhering to resource constraints.

Write a program whose code maximizes the total number of produced beverages ("Lemonade" and "Fruit Juice"), considering the resource limitations.


```
python production_optimization.py

# Output

# Welcome to the CBC MILP Solver 
# Version: 2.10.3 
# Build Date: Dec 15 2019 

# At line 2 NAME          MODEL
# At line 3 ROWS
# At line 9 COLUMNS
# At line 21 RHS
# At line 26 BOUNDS
# At line 29 ENDATA
# Problem MODEL has 4 rows, 2 columns and 5 elements
# Coin0008I MODEL read with 0 errors
# Option for timeMode changed from cpu to elapsed
# Continuous objective value is 50 - 0.00 seconds
# Cgl0004I processed model has 0 rows, 0 columns (0 integer (0 of which binary)) and 0 elements
# Cbc3007W No integer variables - nothing to do
# Cuts at root node changed objective from -50 to -1.79769e+308
# Probing was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# Gomory was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# Knapsack was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# Clique was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# MixedIntegerRounding2 was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# FlowCover was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# TwoMirCuts was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# ZeroHalf was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)

# Result - Optimal solution found

# Objective value:                50.00000000
# Enumerated nodes:               0
# Total iterations:               0
# Time (CPU seconds):             0.00
# Time (Wallclock seconds):       0.00

# Option for printingOptions changed from normal to all
# Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00

# Status: Optimal
# Lemonade to produce: 30.0
# Fruit Juice to produce: 20.0
# Total Production: 50.0
```