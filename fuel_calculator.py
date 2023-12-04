import math
import os
#* Fuel Calculation based on number of pitstops, race length(time or laps), fuel consumption, and laptime
#* Presents calculation for a Safe(full formation lap) or Reccomended and displays # of laps

# TODO: Add master input redundancies and clean up structure
# TODO: Equation simplification
# TODO: Add feature to take fuel tank size into account


#* Terminal line seperation
def line_seperation():
    width = os.get_terminal_size().columns
    print('=' * width)


#* Fuel based on number of laps
def lap_based_fuel():
    while True:
        try:
            pitstops = int(input('Number of pitstops(Input 0 if none): '))
            laps = int(input('Number of laps: '))
            fuel_consumption = float(input('Fuel per lap: '))
            break

        except:
            print('Please enter a numeric value.')
        
    if pitstops.is_integer() and pitstops > 0:
        lap_total = laps
        safe = math.ceil((((laps * fuel_consumption) + (fuel_consumption * 3)) / (pitstops + 1)))
        reccomended = math.ceil((((laps * fuel_consumption) + fuel_consumption) / (pitstops + 1)))

        line_seperation()
        print(f'Total laps: {lap_total}\n')
        print(f'Safe fuel per stint(Formation lap): {safe} liters\n')
        print(f'Reccomended fuel: {reccomended} liters')
        line_seperation()
        quit

    else:
        lap_total = laps
        safe = math.ceil((laps * fuel_consumption) + (fuel_consumption * 3))
        reccomended = math.ceil((laps * fuel_consumption) + fuel_consumption)

        line_seperation()
        print(f'Total laps: {lap_total}\n')
        print(f'Safe fuel(Full formation lap): {safe} liters\n')
        print(f'Reccomended fuel: {reccomended} liters')
        line_seperation()
        quit


#* Fuel based on race time
def time_based_fuel():
    while True:
        try:
            pitstops = int(input('Number of pitstops(Input 0 if none): '))
            time = int(input('Length of race(in minutes): ')) * 60
            fuel_consumption = float(input('Fuel per lap: '))
            minutes, seconds = input('Laptime(minutes:seconds): ').split(':')
            laptime = ((int(minutes)) * 60) + int(seconds)
            break

        except:
            print('Please enter a numeric value or check you input values correctly')
        
    if pitstops.is_integer() and pitstops > 0:
        lap_total = math.ceil(time/ laptime)
        safe = math.ceil(((lap_total * fuel_consumption) + (fuel_consumption * 3) / (pitstops + 1)))
        reccomended = math.ceil(((lap_total * fuel_consumption) + fuel_consumption) / (pitstops + 1))

        line_seperation()
        print(f'Total Laps: {lap_total}\n')
        print(f'Safe fuel per stint(Full formation lap): {safe} liters\n')
        print(f'Reccomended fuel per stint: {reccomended} liters')
        line_seperation()
        quit

    else:
        line_seperation()
        print(f'Total Laps: {lap_total}\n')
        print(f'Safe fuel(Full formation lap): {safe} liters\n')
        print(f'Reccomended fuel: {reccomended} liters')
        line_seperation()
        quit


#* Master executable
def master():
    race_type = str(input('Is this a timed or lap race? ')).lower()
    
    if race_type == 'timed':
        time_based_fuel()
        quit()
    if race_type == 'lap':
        lap_based_fuel()
        quit()
    else:
        print('Please enter a valid input.')


#* Runs program
master()