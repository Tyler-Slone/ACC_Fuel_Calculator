import math
import os
#* Fuel calculation based on number of pitstops, race length(time or laps), fuel consumption, laptime, and fuel tank capacity
#* Displays a safe and recommended quantity of fuel and displays # of laps


#* Global vars
fuel_tank_size = 0
pitstops = 0
laps = 0
fuel_consumption = 0
time = 0
laptime = 0


#* Terminal line seperation
def line_seperation():
    width = os.get_terminal_size().columns
    print('=' * width)




#* Fuel based on number of laps
def lap_based_fuel():
    global fuel_tank_size
    global pitstops
    global laps
    global fuel_consumption


    while True:
        try:
            fuel_tank_size = int(input('What is your max fuel capacity: '))
            pitstops = int(input('Number of pitstops(Input 0 if none): '))
            laps = int(input('Number of laps: '))
            fuel_consumption = float(input('Fuel per lap: '))
            break

        except:
            print('Please enter a numeric value.')
    

    safe = math.ceil(((laps * fuel_consumption) + (fuel_consumption) * 2.5) / (pitstops + 1))
    recommended = math.ceil(((laps * fuel_consumption) + fuel_consumption) / (pitstops + 1))

    if safe > fuel_tank_size:
       small_fueltank_lap()

    else:
        line_seperation()
        print(f'Number of laps: {laps}\n')
        print(f'Safe amount of fuel per stint: {safe} liters\n')
        print(f'Recommended amount of fuel per stint: {recommended} liters')
        line_seperation()


#* Calculation for pitstops and fuel when not enough fueltank capacity based on laps
def small_fueltank_lap():
    global fuel_tank_size
    global pitstops
    global laps
    global fuel_consumption
    
    line_seperation()
    print(f'Your fueltank doesnt have enough capacity for {pitstops} pitstops. Instead use the information below.\n')
    line_seperation()

    minimum = math.ceil(laps * fuel_consumption)
    pitstops = math.ceil(minimum / fuel_tank_size)
    safe = math.ceil((minimum + (fuel_consumption * 2.5)) / (pitstops + 1))
    recommended = math.ceil((minimum + fuel_consumption) / (pitstops + 1))

    line_seperation()
    print(f'Number of laps: {laps}\n')
    print(f'Number of pitstops: {pitstops}\n')
    print(f'Safe amount of fuel per stint: {safe} liters\n')
    print(f'Recommended amount of fuel per stint: {recommended} liters')
    line_seperation()




#* Fuel based on race time
def time_based_fuel():
    global fuel_tank_size
    global pitstops
    global laps
    global fuel_consumption
    global time
    global laptime

    while True:
        try:
            fuel_tank_size = int(input('What is your max fuel capacity: '))
            pitstops = int(input('Number of pitstops(Input 0 if none): '))
            time = int(input('Length of race(in minutes): ')) * 60
            fuel_consumption = float(input('Fuel per lap: '))
            minutes, seconds = input('Laptime(minutes:seconds): ').split(':')
            laptime = ((int(minutes)) * 60) + int(seconds)
            break

        except:
            print('Please enter a numeric value or check you input values correctly')
        
    lap_total = math.ceil(time / laptime)
    safe = math.ceil(((lap_total * fuel_consumption) + (fuel_consumption * 2.5)) / (pitstops + 1))
    recommended = math.ceil(((lap_total * fuel_consumption) + fuel_consumption) / (pitstops +1))

    if safe > fuel_tank_size:
        small_fueltank_time()
    
    else:
        line_seperation()
        print(f'Number of laps: {lap_total}\n')
        print(f'Safe amount of fuel per stint: {safe} liters\n')
        print(f'Recommended amount of fuel per stint: {recommended} liters')
        line_seperation()


#* Calculation for pitstops and fuel when not enough fueltank capacity based on time
def small_fueltank_time():
    global fuel_tank_size
    global pitstops
    global laps
    global fuel_consumption
    global time
    global laptime

    line_seperation()
    print(f'Your fueltank doesnt have enough capacity for {pitstops} pitstops. Instead use information below.\n')
    line_seperation()

    lap_total = math.ceil(time / laptime)
    minimum = math.ceil(lap_total * fuel_consumption)
    pitstops = math.ceil(minimum / fuel_tank_size)
    safe = math.ceil((minimum + (fuel_consumption * 2.5)) / (pitstops + 1))
    recommended = math.ceil((minimum + fuel_consumption) / (pitstops + 1))

    line_seperation()
    print(f'Number of laps: {lap_total}\n')
    print(f'Number of pitstops: {pitstops}\n')
    print(f'Safe amount of fuel per stint: {safe} liters\n')
    print(f'Recommended amount of fuel per stint: {recommended} liters')
    line_seperation()




#* Master executable
def new_main():
    race_type = str(input('Is this a timed or lap race? ')).lower()

    match race_type:
        case 'timed':
            time_based_fuel()
        case 'lap':
            lap_based_fuel()
        case 'quit':
            quit
        case _:
                print('Please enter timed, lap, or quit.')


#* Runs program
if __name__ == '__main__':
    new_main()