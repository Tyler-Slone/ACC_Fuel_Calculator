import math
#* Fuel Calculation based on race duration(laps or time), fuel consumption, and laptime
#* Presents calculation for a Safe(full formation lap) or Reccomended and displays # of laps

# TODO: Add pitstop functionality
# TODO: Use match to simplify maybe


#List of variables for reminder
time = 0
laps = 0
fuel_consumption = 0
laptime = 0
lap_total = 0
safe = 0
recc = 0


#Calculation for fuel based on number of laps
def lap_based_fuel():
    while True:
        try:
            laps = int(input('Number of laps: '))
            fuel_consumption = int(input('Fuel per lap: '))
            break
        except:
            print('Please enter a numeric value.')


    lap_total = laps
    safe = math.ceil((laps * fuel_consumption) + (fuel_consumption * 3))
    recc = math.ceil((laps * fuel_consumption) + fuel_consumption)

    print(f'Total Laps: {lap_total}\n Safe(Full formation lap): {safe} liters\n Reccomended Fuel: {recc} liters')


#Calculation for fuel based on race time
def time_based_fuel():
    while True:
        try:
            time = int(input('Length of race(in minutes): ')) * 60
            fuel_consumption = float(input('Fuel per lap: '))
            minutes, seconds = input('Laptime(minutes:seconds): ').split(':')
            laptime = ((int(minutes)) * 60) + int(seconds)
            break
        except:
            print('Please enter a numeric value or check you input values correctly')

    lap_total = math.ceil(time / laptime)
    safe = math.ceil((lap_total * fuel_consumption) + (fuel_consumption * 3))
    recc = math.ceil((lap_total * fuel_consumption) + fuel_consumption)

    print(laptime)
    print(f'Total Laps: {lap_total}\n Safe(Full formation lap): {safe} liters\n Reccomended Fuel: {recc} liters')
    quit


#Master executable
def master():
    calc = str(input('Is this a timed or lap race? ')).lower()
    if calc == 'timed':
        time_based_fuel()
        quit()
    if calc == 'lap':
        lap_based_fuel()
        quit()
    else:
        print('Please enter a valid input.')


#Runs program
master()