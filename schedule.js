// console.log(employees)

// Global Variables - Cleanup
let employeesNameArr = Object.keys(employees);
let newScheduleArr = Object.keys(newSchedule)


function employeeCycle(str1, str2, prefferedPass, slot) {
    let slotStr = str1;
    let dayStr = str2;
    let slotFilled = true;
    if (slotStr == '') {
        slotFilled = false;
    }
    let prefferedSpent = true;
    for (let emp = 0; emp < employeesNameArr.length; emp++) {
        // console.log(dayStr, slotStr, employeesNameArr[employee])
        let employeeStr = employeesNameArr[emp]
        let employeeAvailable = employees[employeeStr].availability[dayStr].available
        let shiftCount = employees[employeeStr].daysScheduled

        // Preffered spent check
        if (employees[employeeStr].prefferedSpent == false) {
            prefferedSpent = false;
            console.log(employees[employeeStr])
        }
        if (shiftCount >= 2) {
            console.log(employeeStr + ' has the max shifts allocated.' + shiftCount)
        } else {
            if (!employeeAvailable) {
                console.log(employeeStr + ' is not available to work on ' + dayStr)
            } else {
                if (slotFilled) {
                    console.log('Slot is filled by ' + newSchedule[dayStr][slot])
                } else {

                    // Preffered Pass
                    if (prefferedPass && prefferedSpent == false) {
                        // console.log('- preffered pass -')
                        console.log(prefferedSpent)
                        let employeePreffered = employees[employeeStr].availability[dayStr].preffered
                        if (employeePreffered) {
                            newSchedule[dayStr][slot] = employeeStr
                            // console.log('schedule change: ' + employeeStr)
                            employees[employeeStr].prefferedSpent = true;
                            employees[employeeStr].daysScheduled++;
                            slotFilled = true;
                            prefferedSpent = true;
                        } else {

                            // Available Pass
                            prefferedSpent = true;
                            slotFilled = true;
                            employees[employeeStr].daysScheduled++;
                            newSchedule[dayStr][slot] = employeeStr

                        }

                    }

                    // Available Pass


                }

            }
        }


    }
}

function scheduleCycle(slot, prefferedPass) {
    for (let day = 0; day < newScheduleArr.length; day++) {
        // 

        let dayStr = newScheduleArr[day]
        // console.log();
        let slotStr = newSchedule[dayStr][slot]



        employeeCycle(slotStr, dayStr, prefferedPass, slot)




    }
}

// Call
scheduleCycle('slot1', true)
// scheduleCycle('slot2', true)
// scheduleCycle('slot1', false)
// scheduleCycle('slot2', false)
console.log(newSchedule)
console.log(employees)