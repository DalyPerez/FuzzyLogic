from knowledge import Variable, Rule, parse_rule
from fuzzy_system import FuzzySystem
from membership import triangular, trapezoidal
from agregation import Mamdani, Larsen
from defuzzy import centroid, bisector, mean_max, left_max, right_max

fuzzy = FuzzySystem(Mamdani(bisector, lambda x, y: x * y))

#------------------VARIABLES----------------------
v1 = Variable("Traffic")
v1.add_value("Null", triangular(0, 5, 10), (0, 10) )
v1.add_value("Moderate", triangular(7, 15, 23), (7, 23) )
v1.add_value("Intense", triangular(20, 30, 40), (20, 40) )

v2 = Variable("Walkers")
v2.add_value("Low", triangular(0, 5, 10), (0, 10) )
v2.add_value("Medium", triangular(5, 10, 15), (5, 15) )
v2.add_value("High", triangular(10, 20, 30), (10, 30) )

v3 = Variable("GreenDuration")
v3.add_value("Short", triangular(0, 10, 30), (0, 30) )
v3.add_value("Medium", triangular(20, 40, 60), (20, 60) )
v3.add_value("Long", triangular(40, 90, 100), (40, 100) )

fuzzy.add_variable(v1)
fuzzy.add_variable(v2)
fuzzy.add_variable(v3)

# v1.plot()
# v2.plot()
# v3.plot()

#---------------RULES-----------------------
r1 = parse_rule("Walkers is Medium and Traffic is Moderate => GreenDuration is Medium") 
r2 = parse_rule("Walkers is Low and Traffic is Intense => GreenDuration is Short") 


fuzzy.add_rule(r1)
fuzzy.add_rule(r2)

input_var = {"Walkers": 7 , "Traffic": 22 }

fuzzy.inference(input_var)


