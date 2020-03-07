# Create employees as dictionaries with the following required Key Values
# employeeName: String
# employeeID: Integer
# availability: Dictionary


# TEST DATA. Real data will be collected with inputs.
aram = {
    "employeeName": "Aram",
    "employeeID": 0,
    "daysScheduled": 0,
    "prefferedSpent": False,
    "availability":  {
        "Monday": {
            "available": True,
            "preffered": False,
        },
        "Tuesday": {
            "available": True,
            "preffered": False,
        },
        "Wednesday": {
            "available": True,
            "preffered": False,
        },
        "Thursday": {
            "available": True,
            "preffered": True,
        },
        "Friday": {
            "available": True,
            "preffered": False,
        },
        "Saturday": {
            "available": True,
            "preffered": True,
        },
    },
}

penny = {
    "employeeName": "Penny",
    "employeeID": 1,
    "daysScheduled": 0,
    "prefferedSpent": False,
    "availability":  {
        "Monday": {
            "available": True,
            "preffered": True,
        },
        "Tuesday": {
            "available": True,
            "preffered": False,
        },
        "Wednesday": {
            "available": True,
            "preffered": False,
        },
        "Thursday": {
            "available": True,
            "preffered": False,
        },
        "Friday": {
            "available": True,
            "preffered": True,
        },
        "Saturday": {
            "available": True,
            "preffered": False,
        }
    },
}

chris = {
    "employeeName": "Chris",
    "employeeID": 2,
    "daysScheduled": 0,
    "prefferedSpent": False,
    "availability":  {
        "Monday": {
            "available": True,
            "preffered": True,
        },
        "Tuesday": {
            "available": True,
            "preffered": True,
        },
        "Wednesday": {
            "available": True,
            "preffered": False,
        },
        "Thursday": {
            "available": True,
            "preffered": False,
        },
        "Friday": {
            "available": True,
            "preffered": False,
        },
        "Saturday": {
            "available": True,
            "preffered": True,
        },
    }
}

# Array of employees
employees = [aram, penny, chris]

# Returns an output of all employees availability
# Comment out for readability
# for day in employees:
#     print('Employee: ', x['employeeName'])
#     print('ID: ', x['employeeID'])
#     for shift, y in x['availability'].items():
#         print(shift)
#         print('Available: ', y['available'])
#         print('Preffered: ', y['preffered'])

#     print('')

#     print('Generating new schedule')

# Logic area
TOTAL_SHIFTS = 12
maxShifts = round(TOTAL_SHIFTS / len(employees))
print('Shifts per sensei: ', maxShifts)

# Generate new Schedule
newSchedule = {
    "Monday": {
        "slot1": "",
        "slot2": "",
    },
    "Tuesday": {
        "slot1": "",
        "slot2": "",
    },
    "Wednesday": {
        "slot1": "",
        "slot2": "",
    },
    "Thursday": {
        "slot1": "",
        "slot2": "",
    },
    "Friday": {
        "slot1": "",
        "slot2": "",
    },
    "Saturday": {
        "slot1": "",
        "slot2": "",
    },
}

print(newSchedule["Monday"]["slot1"])
# This will be the test pass. It will go through each employees availability to see if there are any days where no one can work, or less than the required amount. If it is


# For the first pass, we will iterate through the every day and every slot of the schedule we are creating. Right now it is an array order (will do priority check for fairness)
# If the slot is open, will parse through employees to see if their priority is that day. If it is, they will be placed in that slot.
# This will be a recursive function. If the function goes through each slot after checking the availability of each employee and cannot fill, it will break the loop.

for day, slot in newSchedule.items():
    # Lets check what we are working with here to make sure that it is iterating through the correct data structure
    print(day)
    # print(slot["slot1"] == "")
    slot1 = slot["slot1"]
    slot2 = slot["slot2"]
    for z in employees:
        employeeName = z["employeeName"]
        employeeID = z["employeeID"]
        # prefferedSpent = z["prefferedSpent"]
        for shift, y in z['availability'].items():
            preffered = y["preffered"]
            available = y["available"]
            if shift == day:
                if preffered & available:
                    # print(employeeName, " is preffered to work on", day)

                    if slot1 == "":
                        if slot1 != employeeName:
                            if employees[employeeID]["daysScheduled"] <= 2:
                                if employees[employeeID]["prefferedSpent"] == False:
                                    # print('That slot1 is empty boi')
                                    slot1 = employeeName
                                    newSchedule[day]["slot1"] = slot1
                                    # print()
                                    employees[employeeID]["daysScheduled"] += 1
                                    employees[employeeID]["prefferedSpent"] = True

                    if slot2 == "":
                        if slot1 != employeeName:
                            if slot2 != employeeName:
                                if employees[employeeID]["daysScheduled"] <= 2:
                                    if employees[employeeID]["prefferedSpent"] == False:
                                        slot2 = employeeName
                                        newSchedule[day]["slot2"] = slot2
                                        employees[employeeID]["daysScheduled"] += 1
                                        employees[employeeID]["prefferedSpent"] = True
# print(employees[0]["daysScheduled"])
print(newSchedule)
# For the second pass, we will go through each slot again. If the slot was not filled in the priority pass, we will parse through the employees again to see if they are available.
# This will be a recursive function. If the function goes through each slot after checking the availability of each employee and cannot fill, it will break the loop.

# The last pass will check to see if there are any open slots. If there are, it will go through and see if any employee has avaibility in both days, and if it can rearrange the schedule
# If it cannot, an error code will be submitted for a manual fix of those days.
