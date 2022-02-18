# Work from Home - Hour tracker
def Menu():

    while(True):
        option = None

        print("""Welcome to WFH Hours Tracker
Please choose from the following options:

+----------------+
 Menu
+----------------+
 [h] Log Hours
 [r] Print Report
 [q] Quit
      """)
        options = input("Enter selection: ")

        if options == 'h':
            Submit_Hours()
        elif options == 'r':
            Create_Report()
        elif options == 'q':
            print("\nCheerio. \n")
            break
        else:
            print("Please enter a valid selection.")


def Submit_Hours():
    min_daily_hours = 6
    max_daily_hours = 9
    min_weekly_hours = 32
    max_weekly_hours = 40
    good_min_weekly_hours = 36
    good_max_weekly_hours = 38

    worked_hours = {
        "WeekNumber": "",
        "EmployeeID": "",
        "EmployeeName": "",
        "Monday": "",
        "Tuesday": "",
        "Wednesday": "",
        "Thursday": "",
        "Friday": "",
        }

    starting_day = 3

    weekly_report = {
        "Employee 1": 0,
        "Employee 2": 0,
        "Employee 3": 0,
        "Employee 4": 0,
        "Employee 5": 0,
        "Employee 6": 0,
        "Employee 7": 0,
        }

    for employee_count, employee_number in enumerate(weekly_report):
        print()
        print()
        print("+---------------------------+")
        print(" Enter details of Employee", employee_count + 1)
        print("+---------------------------+")
        worked_hours["WeekNumber"] = "Week " + \
            str(input("\nCurrent working week number >> "))
        print()
        worked_hours["EmployeeID"] = str(input("Employee ID >> "))
        print()
        worked_hours["EmployeeName"] = str(
            input("Employee's name >> "))
        print()

        print("+----------------------------------+")
        print(" Enter hours per day for employee",
              worked_hours["EmployeeName"])
        print("+----------------------------------+")

        for count, Day in enumerate(worked_hours):
            if count >= starting_day:
                print()
                print("Hours worked on", Day, ">> ", end='')
                worked_hours[Day] = str(input())
        print()
        ID_name_week_for_heading = "ID: "
        ID_name_week_for_heading = ID_name_week_for_heading + \
            worked_hours["EmployeeID"]
        ID_name_week_for_heading = ID_name_week_for_heading + " Name: "
        ID_name_week_for_heading = ID_name_week_for_heading + \
            worked_hours["EmployeeName"]
        ID_name_week_for_heading = ID_name_week_for_heading + " "
        ID_name_week_for_heading = ID_name_week_for_heading + \
            worked_hours["WeekNumber"]

        print("+-----------------------------------------+")
        print(" Summary for Employee", ID_name_week_for_heading)
        print("+-----------------------------------------+")
        day_within_limits_flag = 0

        total_hours = 0
        for count, Day in enumerate(worked_hours):
            if count >= starting_day:
                total_hours = total_hours + int(worked_hours[Day])
                if int(worked_hours[Day]) < min_daily_hours:
                    day_within_limits_flag = 1
                    print(worked_hours["EmployeeName"],
                          "was watching the grass grow on", Day)
                elif int(worked_hours[Day]) > max_daily_hours:
                    day_within_limits_flag = 1
                    print(worked_hours["EmployeeName"],
                          "was busier than a one-legged man in an arse-kicking competition on", Day)
            else:
                pass
        if day_within_limits_flag == 0:
            print(worked_hours["EmployeeName"],
                  "has kicked it over the black dot.")

        print(worked_hours["EmployeeName"], "had their nose to the grindstone for a total of",
              total_hours, "hours in", worked_hours["WeekNumber"])

# Part B)
        weekly_report[employee_number] = total_hours
        if total_hours < min_weekly_hours:
            print(worked_hours["EmployeeName"],
                  "must have been as crook as Rookwood in", worked_hours["WeekNumber"])
        elif total_hours > max_weekly_hours:
            print(worked_hours["EmployeeName"],
                  "was busier than a one armed monkey with two bananas in", worked_hours["WeekNumber"])
        else:
            print(worked_hours["EmployeeName"], "made a bird of it.")

        print()
        file_csv_out = "DailyHours_DB.csv"

        with open(file_csv_out, "a") as file:
            str_buffer = ",".join(worked_hours.values())
            str_buffer = str_buffer + '\n'
            file.write(str_buffer)

    insufficient_hours = 0
    excessive_hours = 0
    appropriate_hours = 0

    for employee_number_counter_2 in weekly_report:
        if weekly_report[employee_number_counter_2] < min_weekly_hours:

            insufficient_hours = insufficient_hours + 1
        elif weekly_report[employee_number_counter_2] > max_weekly_hours:

            excessive_hours = excessive_hours + 1
        elif (weekly_report[employee_number_counter_2]
              > good_min_weekly_hours) and (int(weekly_report[employee_number_counter_2])
                                            < good_max_weekly_hours):
            appropriate_hours = appropriate_hours + 1
        else:
            pass

# Part E)
    print("+----------------------+")
    print(" Weekly Employee Report")
    print("+----------------------+")
    print(insufficient_hours, "employees were watching the paint dry")
    print(excessive_hours, "employees worked more than 40 hours a week")
    print(appropriate_hours,
          "employees worked between 30-40 hours a week")

    print()
    input("Press [Enter] to return to the MENU...")

    return None


def Create_Report():

    file_csv_in = "DailyHours_DB.csv"
    csv_list = []

    try:
        with open(file_csv_in, "r") as file:
            for buffer in file:
                buffer = buffer.strip('\n')

                buffer_list = buffer.split(',')
                csv_list.append(buffer_list)
        print()
        print("+-------------------+")
        print(" Worked Hours Report")
        print("+-------------------+")
        print()
        options = input('How many reports would you like to display >> ')
        print()
        if len(csv_list) < int(options):
            int_rep_number = len(csv_list)
        else:
            int_rep_number = int(options)

        report_start = len(csv_list) - 1
        report_stop = len(csv_list) - int_rep_number - 1
        report_step = -1

        for i in range(report_start, report_stop, report_step):
            for j in range(len(csv_list[i])):
                print(csv_list[i][j], end=" ")

            print()
        print()
        input("Press [Enter] to return to the MENU...")
        return None

    except FileNotFoundError:
        print("The CSV file has not yet been created.")
        print("Please select Option 1 from the Menu")
        print("to start the data entry.")
        input("Press [Enter] to return to the MENU...")
        return None

Menu()
