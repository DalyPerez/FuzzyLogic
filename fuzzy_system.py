class FuzzySystem:
    def __init__(self, agregation_method):
        self.variables = {}
        self.rules = []
        self.agregation_method = agregation_method

    def add_variable(self, variable):
        self.variables[variable.name] = variable
    
    def add_rule(self, rule):
        self.rules.append(rule)

    def fuzzification(self, input_var_values):
        """
            input_var_values: dict {var_name: var_value}
            return: 
        """
        umbrals = []
        
        for r in self.rules:
            u = 1
            for c in r.antecedents:
                name, value = c
                input_value = input_var_values[name]
                u = min(u, self.variables[name].values[value](input_value))
                print(name, value, input_value, u)
            umbrals.append(u)
        return umbrals

    def inference(self, input_var_values):
        """
            input_var_values: dict {var_name: var_value}
        """
        umbral_corts = self.fuzzification(input_var_values)
        self.agregation_method.predict(self.variables, umbral_corts, self.rules)
        

if __name__ == "__main__":
    fuzzy = FuzzySystem()
