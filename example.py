from knowledge import Variable, Rule
from fuzzy_system import FuzzySystem
from membership import triangular, trapezoidal
from agregation import Mamdani

fuzzy = FuzzySystem(Mamdani(None))

#------------------VARIABLES----------------------
v1 = Variable("Traffic")
v1.add_value("Null", triangular(0, 5, 10) )
v1.add_value("Moderate", triangular(7, 15, 23) )
v1.add_value("Intense", triangular(20, 30, 40) )

v2 = Variable("Walkers")
v2.add_value("Low", triangular(0, 5, 10) )
v2.add_value("Medium", triangular(5, 10, 15) )
v2.add_value("High", triangular(10, 20, 30) )

v3 = Variable("GreenDuration")
v3.add_value("Short", triangular(0, 10, 20) )
v3.add_value("Medium", triangular(20, 40, 60) )
v3.add_value("Long", triangular(40, 90, 100) )

fuzzy.add_variable(v1)
fuzzy.add_variable(v2)
fuzzy.add_variable(v3)

# v1.plot()
# v2.plot()
# v3.plot()

#---------------RULES-----------------------
r1 = Rule()
r1.add_antecedent("Walkers", "Medium")
r1.add_antecedent("Traffic", "Moderate")
r1.add_consequent("GreenDuration", "Medium")

r2 = Rule()
r2.add_antecedent("Walkers", "Low")
r2.add_antecedent("Traffic", "Intense")
r2.add_consequent("GreenDuration", "Short")

fuzzy.add_rule(r1)
fuzzy.add_rule(r2)

input_var = {"Walkers": 7 , "Traffic": 22 }

fuzzy.inference(input_var)


