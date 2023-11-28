import math
#* Fuel Calculation based on race duration(laps or time), fuel consumption, and laptime
#* Present calculation for a Safe(full formation lap) or Reccomended and also display # of laps
#! Fix time calculation input/ calculation

time = 0
laps = 0
fuel_consumption = 0
laptime = 0
lap_total = 0
safe = 0
recc = 0

def lap_based_fuel():
    try:
        laps = float(input('Number of laps: '))
        fuel_consumption = float(input('Fuel per lap: '))
        laptime = float(input('Laptime: '))
    except:
        print('Please enter a numeric value.')
        quit()


    lap_total = laps
    safe = math.ceil((laps * fuel_consumption) + (fuel_consumption * 3))
    recc = math.ceil((laps * fuel_consumption) + fuel_consumption)

    print(f'Total Laps: {lap_total}\n Safe(Full formation lap): {safe} liters\n Reccomended Fuel: {recc} liters')


def time_based_fuel():
    try:
        time = float(input('Length of race:'))
        fuel_consumption = float(input('Fuel per lap:'))
        laptime = float(input('Laptime:'))
    except:
        print('Please enter a numeric value.')
        quit()
    
    lap_total = math.ceil(time / laptime)
    safe = math.ceil((lap_total * fuel_consumption) + (fuel_consumption * 3))
    recc = math.ceil((lap_total * fuel_consumption) + fuel_consumption)

    print(f'Total Laps: {lap_total}\n Safe(Full formation lap): {safe} liters\n Reccomended Fuel: {recc} liters')

def master():
    calc = str(input('Is this a timed or lap race?')).lower()
    if calc == 'timed':
        time_based_fuel()
    elif calc == 'lap':
        lap_based_fuel()
    else:
        print('Please enter a valid input.')
        quit()


master()