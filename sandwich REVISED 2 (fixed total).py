"""Sophanda Long.
This code will ask users for
their sandwich preferences."""

import pyinputplus as pyip
print('Sandwich Maker Program.')

# Organization
def main():
    try:
        food_price, order, others, other_food, sandwiches, total_price = inputs()
        outputs(food_price, order, total_price, sandwiches)
        restart = input('Need more sandwiches? Enter y or n: ')
        if restart == 'y':
            print('OK')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)


# Asking user what they want in their sandwich
def inputs():
    food_price = {'white': 2.00, 'wheat': 2.00, 'sourdough': 2.00,
                  'chicken': 3.00, 'turkey': 2.50, 'ham': 1.50, 'tofu': 3.00,
                  'cheddar': 1.00, 'swiss': 1.00, 'mozzarella': 1.00,
                  'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.50, 'tomatoes': 0.50
                  }
    order = []
    others = ['mayo', 'mustard', 'lettuce', 'tomatoes']
    total_price = 0.00

    bread = pyip.inputMenu(['white', 'wheat', 'sourdough'], 'What type of bread would you like?\n', lettered=True)
    order.append(bread)

    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],'What type of protein would you like?\n' , lettered=True)
    order.append(protein)

    cheese = pyip.inputYesNo('Do you want cheese (yes or no)? ')
    if cheese == 'yes':
        cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], 'What type of cheese would you like?\n' , lettered=True)
        order.append(cheese_type)
    else:
        print('No cheese.')

    other_food = ''
    for index in others:
        other_food = pyip.inputYesNo('Would you like ' + index + ' (yes or no)?\n')
        if other_food == 'yes':
            order.append(index)
        else:
            print('No', index)

    sandwiches = pyip.inputInt('How many sandwiches would you like? ', min=1)
    return food_price, order, others, other_food, sandwiches, total_price


# Displaying the results and calculating total
def outputs(food_price, order, total_price, sandwiches):
    for food in order:
        if food in food_price:
            total_price += food_price.get(food)
            print(f'{food:<20}' + '$' + str('{:0.2f}'.format(food_price.get(food))))

    sandwich_total = total_price * sandwiches
    print('Number of sandwiches: ' + str(sandwiches))
    print('\n')
    print('Sandwich total: $' + str('{:0.2f}'.format(sandwich_total)))

main()
