# coffee_machine-using-python-project-

Coffee Machine-:
    This is a simple coffee machine simulation program implemented in Python. It allows users to select various types of coffee drinks and manages the inventory of ingredients.

Features:-->
    Choose from a menu of coffee drinks: espresso, cappuccino, latte.
    Check the availability of ingredients.
    Dispense the selected coffee drink.
    Update the inventory of ingredients after dispensing.
Prerequisites:->
         Python 3.x
         random module (included in Python standard library)

    pseudocde of coffe_machine____
 

sql
Copy code
Start

Display menu options
Get user choice

If user choice is valid:
    Check if there are enough ingredients

    If there are enough ingredients:
        Deduct the required amount of ingredients from the inventory
        Calculate the cost of the selected drink
        Prompt the user to insert coins

        If the user inserts enough coins:
            Calculate the change
            Dispense the selected drink
            Dispense the change
            Serve the drink

        If the user does not insert enough coins:
            Display an error message
            Cancel the transaction
            Return the coins

    If there are not enough ingredients:
        Display an error message
        Return to the menu

If user choice is not valid:
    Display an error message
    Return to the menu

Repeat the process until the user chooses to exit

End
