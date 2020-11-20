from knowledge import Variable, Rule, parse_rule
from fuzzy_system import FuzzySystem
from membership import triangular, trapezoidal
from agregation import Mamdani, Larsen
from defuzzy import centroid, bisector, mean_max, left_max, right_max

fuzzy = FuzzySystem(Mamdani(centroid, min))

#------------------VARIABLES----------------------
v1 = Variable("Traffic")
v1.add_value("Null", triangular(0, 5, 10), (0, 10) )
v1.add_value("Moderate", trapezoidal(5, 10, 20, 25), (5, 25) )
v1.add_value("Intense", triangular(15, 25, 35), (15, 35) )

v2 = Variable("Walkers")
v2.add_value("Low", triangular(0, 3, 6), (0, 6) )
v2.add_value("Medium", trapezoidal(4, 6, 12, 14), (4, 14) )
v2.add_value("High", triangular(10, 15, 20), (10, 20) )

v3 = Variable("GreenDuration")
v3.add_value("Short", triangular(0, 10, 20), (0, 20) )
v3.add_value("Medium", trapezoidal(15, 30, 40, 50), (15, 60) )
v3.add_value("Long", triangular(40, 70, 100), (40, 100) )

fuzzy.add_variable(v1)
fuzzy.add_variable(v2)
fuzzy.add_variable(v3)

# v1.plot()
# v2.plot()
# v3.plot()

#---------------RULES-----------------------
r1 = parse_rule("Walkers is Low and Traffic is Null => GreenDuration is Medium") 
r2 = parse_rule("Walkers is Low and Traffic is Moderate => GreenDuration is Short") 
r3 = parse_rule("Walkers is Low and Traffic is Intense => GreenDuration is Long") 
r4 = parse_rule("Walkers is Medium and Traffic is Null => GreenDuration is Short") 
r5 = parse_rule("Walkers is Medium and Traffic is Moderate => GreenDuration is Medium") 
r6 = parse_rule("Walkers is Medium and Traffic is Intense => GreenDuration is Medium") 
r7 = parse_rule("Walkers is High and Traffic is Null => GreenDuration is Short") 
r8 = parse_rule("Walkers is High and Traffic is Moderate => GreenDuration is Medium") 
r9 = parse_rule("Walkers is High and Traffic is Intense => GreenDuration is Long") 

fuzzy.add_rule(r1)
fuzzy.add_rule(r2)
fuzzy.add_rule(r3)
fuzzy.add_rule(r4)
fuzzy.add_rule(r5)
fuzzy.add_rule(r6)
fuzzy.add_rule(r7)
fuzzy.add_rule(r8)
fuzzy.add_rule(r9)

input_var = {"Walkers": 7 , "Traffic": 22 }

fuzzy.inference(input_var)


