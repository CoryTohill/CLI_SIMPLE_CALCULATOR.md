import re


class Calc():
    def __init__(self):
        self.counter = 0
        self.last_answer = None
        self.last_entry = None
        self.variable_dict = dict()

        # lexicon of math functions based on which operand is used
        self.operators_dict = {
            '+': lambda num1, num2: num1 + num2,
            '-': lambda num1, num2: num1 - num2,
            '/': lambda num1, num2: num1 / num2,
            '%': lambda num1, num2: num1 % num2,
            '*': lambda num1, num2: num1 * num2,
        }

    def show_greeting(self):
        """ Displays the initial program greeting and calls the show_help method

        Method arguments:
        -----------------
        n/a
        """
        print("Welcome to the Simple Interactive Calculator!")
        print("")
        self.show_help()

    def show_help(self):
        """ Displays the help menu

        Method arguments:
        -----------------
        n/a
        """
        print("Enter a mathematical expression to evaluate it. (ex. 2+5)")
        print("")
        print("Store variables by entering a name and value. (ex. Var=7)")
        print("")
        print("Alternate Commands:")
        print("'last' -- displays the last answer")
        print("'lastq' -- displays the last entry/command")
        print("'help' -- displays this menu")
        print("'quit' -- exits the program")
        print("")

    def prompt(self):
        """ Shows the prompt for user input

        Method arguments:
        -----------------
        n/a
        """
        user_input = input("[{}]> ".format(self.counter))

        if user_input == 'quit':
            quit()

        elif user_input == 'help':
            self.show_help()

        elif user_input == 'last':
            print(self.last_answer)

        elif user_input == 'lastq':
            print(self.last_entry)

        # if an equal sign is present, attempt to add a variable to the variable_dict lexicon
        elif "=" in user_input:
            try:
                parsed_input = re.split("[=]", user_input)
                self.set_variable(*parsed_input)
                self.last_entry = user_input
                self.count()

            except (ValueError, TypeError) as error:
                print(type(error).__name__)
                print('Invalid input, please try again.')

        # attempt to parse the user input and pass it to the calculate function
        else:
            try:
                parsed_input = re.split("([+-/%*])", user_input)
                print(self.calculate(*parsed_input))
                self.last_entry = user_input
                self.count()

            except (ValueError, TypeError) as error:
                print(type(error).__name__)
                print("Invalid input, please try again.")

        self.prompt()

    def calculate(self, num1, operator, num2):
        """ Returns the result of a calculation

        Method arguments:
        -----------------
        num1(str) -- The first number/variable name in the calculation
        operator(str) -- The operand to be used, acceptable inputs: +,-,/,%,*
        num2(str) -- The first number/variable name in the calculation
        """
        # if num1 or num2 are in the variable dictionary, set them to be the value in the dictionary
        if num1.lower() in self.variable_dict.keys():
            num1 = self.variable_dict[num1.lower()]

        if num2.lower() in self.variable_dict.keys():
            num2 = self.variable_dict[num2.lower()]

        # converts num1 and num2 to integers before passing them into operators_dict
        # calls function in operators_dict based on operator key passed in
        answer = self.operators_dict[operator](int(num1), int(num2))
        self.last_answer = answer
        return answer

    def count(self):
        """ Adds 1 to the counter used in the prompt

        Method arguments:
        -----------------
        n/a
        """
        self.counter += 1

    def set_variable(self, var, num):
        """ Stores a variable name and it's associated value in an internal lexicon

        Method arguments:
        -----------------
        var(str) -- The variable name
        num(str) -- The number to be associated with the variable name
        """
        var = var.lower()
        num = int(num)

        if var in self.variable_dict.keys():
            print('Error! Variable already exists!')

        elif var.isalpha() is False:
            raise TypeError("Variable name must consist of alphabetic characters only!")

        else:
            self.variable_dict[var] = num


if __name__ == '__main__':
    Calc().show_greeting()
    Calc().prompt()
