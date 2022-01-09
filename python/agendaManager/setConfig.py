# Load the function for saving the configuraiton
from agendaConfigurator import setConfig

# Configuration variables
habits = ['Run', 'Journal', 'Test']
meal = 'Leftovers'
day = ['Calendar', 'Tasks', 'Expenses', 'Journal']

# Save the variables to the file
setConfig('habits', habits)
setConfig('meal', meal)
setConfig('day', day)
