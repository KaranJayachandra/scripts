from datetime import datetime, date, timedelta
from calendar import monthrange
from agendaConfigurator import getConfig
    
def createHabitTracker(habits, days):
    
    # Initializing the output variable
    outputString = ''

    # Find the expected length of the first column
    columnWidth = len(max(habits, key=len))
    columnWidth = max(5, columnWidth)

    # Create a header line
    adjustSize = columnWidth - 5
    outputString += '| Habit' + (' ' * adjustSize) + ' |'
    for day in range(days):
        day = day + 1
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        outputString += day + '|'
    outputString += '\n' 

    # Add seperator line
    adjustSize = columnWidth + 2
    outputString += '|' + ('-' * adjustSize) + '|'
    for day in range(days):
        outputString += '--|'
    outputString += '\n'
    
    # Create the habit lines
    for habit in habits:
        adjustSize = columnWidth - len(habit)
        outputString += '| ' + habit + (' ' * adjustSize) + ' |'
        for day in range(days):
            outputString += ' .|'
        outputString += '\n'
    
    # Return the created string
    return outputString

def createMealPlanner(defaultMeal):
    
    # Initializing the output variable
    outputString = ''

    # Creating a list of weekdays
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
   
    # Find the length of the first column
    columnWidth = len(max(days, key=len))

    # Create the header line
    adjustSize = columnWidth - 3
    outputString += '| Day' + (' ' * adjustSize) + ' |'
    adjustSize = len(defaultMeal) - 5
    outputString += ' Lunch' + (' ' * adjustSize) + ' |'
    adjustSize = len(defaultMeal) - 6
    outputString += ' Dinner' + (' ' * adjustSize) + ' |\n'

    # Add seperator line
    outputString += '|' + ('-' * (columnWidth + 2)) + '|'
    outputString += ('-' * (len(defaultMeal) + 2)) + '|'
    outputString += ('-' * (len(defaultMeal) + 2)) + '|\n'

    # Add the meal lines
    for day in days:
        adjustSize = columnWidth - len(day)
        outputString += '| ' + day + (' ' * adjustSize) + ' |'
        outputString += (' ' + defaultMeal + ' |') * 2
        outputString += '\n'

    # Return the value
    return outputString

def createDayPlanner(sections):

    # Initializing the output variable
    outputString = '\n'

    # Writing the sections
    for section in sections:
        outputString += section + ':\n- [ ] \n\n'

    # Return the value
    return outputString

def createWeekSpread(dates):

    # Initializing the output variable
    outputString = ''

    # Create the main header
    outputString += 'Goals:\n- [ ] \n\n'
    outputString += 'Meal Planner:\n\n'
    outputString += createMealPlanner(getConfig('meal')) + '\n'

    # Create the daily spreads
    for date in dates:
        outputString += '### ' + date + '\n'
        outputString += createDayPlanner(getConfig('day'))

    # Return the value
    return outputString

def createMonthSpread():

    # Initializing the output variable
    outputString = '# ' + datetime.today().strftime('%B') + '\n\n'

    # Add lines for goals
    outputString += 'Goals:\n-[ ] \n\n'

    # Get details about the month
    currentYear = datetime.now().year
    currentMonth = datetime.now().month
    totalDays = monthrange(currentYear, currentMonth)[1]     
    
    # Add the habit tracker
    outputString += createHabitTracker(getConfig('habits'), totalDays) + '\n'
    
    # Create a list of dates
    firstDate = date(currentYear, currentMonth, 1)
    lastDate = date(currentYear, currentMonth, totalDays)
    delta = lastDate - firstDate
    dates = [(firstDate + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]

    # Get week number of each date
    weekNumber = [(firstDate + timedelta(days=i)).isocalendar()[1] for i in range(delta.days + 1)]
    uniqueWeekNumber = list(set(weekNumber))
    
    # Loop through each week and create week spreads
    for week in uniqueWeekNumber:
        dateIdx = [i for i, weekOfDate in enumerate(weekNumber) if weekOfDate == week]
        datesInWeek = [date for date, weekOfDate in zip(dates, weekNumber) if weekOfDate == week]
        outputString += '## Week ' + str(week) + '\n\n'
        outputString += createWeekSpread(datesInWeek)

    # Open the file to write to
    with open(datetime.now().strftime('%Y-%m') + '.md', 'w') as agendaFilePointer:
        agendaFilePointer.write(outputString)
        agendaFilePointer.flush()
        agendaFilePointer.close()


