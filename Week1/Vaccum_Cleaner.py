def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum (A or B): ").upper() 
    status_input = input("Enter status of " + location_input + " (0 for Clean, 1 for Dirty): ")
    status_input_complement = input("Enter status of the other room (0 for Clean, 1 for Dirty): ")

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        print("Vacuum is placed in Location A")

        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            cost += 1
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")
        else:
            print("Location A is already clean.")

        if status_input_complement == '1':
            print("Location B is Dirty.")
            print("Moving right to Location B.")
            cost += 1
            print("Cost for moving RIGHT: " + str(cost))
            goal_state['B'] = '0'
            cost += 1
            print("Cost for SUCK: " + str(cost))
            print("Location B has been Cleaned.")
        else:
            print("Location B is already clean.")

    elif location_input == 'B':
        print("Vacuum is placed in Location B")

        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            cost += 1
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")
        else:
            print("Location B is already clean.")

        if status_input_complement == '1':
            print("Location A is Dirty.")
            print("Moving left to Location A.")
            cost += 1
            print("Cost for moving LEFT: " + str(cost))
            goal_state['A'] = '0'
            cost += 1
            print("Cost for SUCK: " + str(cost))
            print("Location A has been Cleaned.")
        else:
            print("Location A is already clean.")

    print("GOAL STATE: " + str(goal_state))
    print("Performance Measurement (Total Cost): " + str(cost))

vacuum_world()