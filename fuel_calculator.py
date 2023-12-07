import math
import os
#* Fuel Calculation based on number of pitstops, race length(time or laps), fuel consumption, and laptime
#* Presents calculation for a Safe(full formation lap) or Reccomended and displays # of laps

#TODO: Add feature to take fuel tank size into account(basic)
#TODO: Have fuel tank size effect number of pitstops
#TODO: Look over wording
#TODO: Equation simplification to reduce parenthesis blindness and adjust safe fuel calculation

#! small_fueltank not working correclty didnt take into consideration matching fuel tank size 
#! and calculations are coming out wrong

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
    

    if (laps * fuel_consumption) > fuel_tank_size:
        small_fueltank_lap()

    elif pitstops.is_integer() and pitstops > 0:
        lap_total = laps
        safe = math.ceil((((laps * fuel_consumption) + (fuel_consumption * 3)) / (pitstops + 1)))
        recommended = math.ceil((((laps * fuel_consumption) + fuel_consumption) / (pitstops + 1)))

        line_seperation()
        print(f'Total laps: {lap_total}\n')
        print(f'Safe fuel per stint(Formation lap): {safe} liters\n')
        print(f'Recommended fuel: {recommended} liters')
        line_seperation()

    else:
        lap_total = laps
        safe = math.ceil((laps * fuel_consumption) + (fuel_consumption * 3))
        recommended = math.ceil((laps * fuel_consumption) + fuel_consumption)

        line_seperation()
        print(f'Total laps: {lap_total}\n')
        print(f'Safe fuel(Full formation lap): {safe} liters\n')
        print(f'Recommended fuel: {recommended} liters')
        line_seperation()


#* Override for not enough fueltank capacity based on laps
def small_fueltank_lap():
    global fuel_tank_size
    global pitstops
    global laps
    global fuel_consumption

    print(f'Your fueltank is not big enough for {pitstops} pitstops. Heres how many pitstops and how much fuel you should get for each stint.\n')

    pitstops = math.ceil((fuel_consumption * laps) / fuel_tank_size)
    lap_total = laps
    safe = math.ceil((((laps * fuel_consumption) + (fuel_consumption * 3)) / (pitstops + 1)))
    recommended = math.ceil((((laps * fuel_consumption) + fuel_consumption) / (pitstops + 1)))

    line_seperation()
    print(f'Total laps: {lap_total}\n')
    print(f'Number of pitstops: {pitstops}\n')
    print(f'Safe fuel per stint(Formation lap): {safe} liters\n')
    print(f'Recommended fuel: {recommended} liters')
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


    if ((time / laptime) * fuel_consumption) > fuel_tank_size:
        small_fueltank_time()
        
    elif pitstops.is_integer() and pitstops > 0:
        lap_total = math.ceil(time / laptime)
        safe = math.ceil(((lap_total * fuel_consumption) + (fuel_consumption * 3) / (pitstops + 1)))
        recommended = math.ceil((((lap_total * fuel_consumption) + fuel_consumption)) / (pitstops + 1))

        line_seperation()
        print(f'Total Laps: {lap_total}\n')
        print(f'Safe fuel per stint(Full formation lap): {safe} liters\n')
        print(f'Recommended fuel per stint: {recommended} liters')
        line_seperation()
        

    else:
        lap_total = math.ceil(time / laptime)
        safe = math.ceil((lap_total * fuel_consumption) + (fuel_consumption * 3))
        recommended = math.ceil((lap_total * fuel_consumption) + fuel_consumption)

        line_seperation()
        print(f'Total Laps: {lap_total}\n')
        print(f'Safe fuel(Full formation lap): {safe} liters\n')
        print(f'Recommended fuel: {recommended} liters')
        line_seperation()
        

#* Override for not enough fueltank capacity based on time
def small_fueltank_time():
    global fuel_tank_size
    global pitstops
    global laps
    global fuel_consumption
    global time
    global laptime

    print(f'Your fueltank is not big enough for {pitstops} pitstops. Heres how many pitstops and hownmuch fuel you should get for each stint.\n')

    lap_total = math.ceil(time / laptime)
    pitstops = math.ceil((fuel_consumption * lap_total) / fuel_tank_size)
    safe = math.ceil((lap_total * fuel_consumption) + (fuel_consumption * 3))
    recommended = math.ceil((lap_total * fuel_consumption) + fuel_consumption)

    line_seperation()
    print(f'Total laps: {lap_total}\n')
    print(f'Number of pitstops: {pitstops}\n')
    print(f'Safe fuel per stint(Formation lap): {safe} liters\n')
    print(f'Recommended fuel: {recommended} liters')
    line_seperation()




#* Master executable
# def main():
#     while True:
#         race_type = str(input('Is this a timed or lap race? ')).lower()

#         if race_type == 'timed':
#             time_based_fuel()
#             break
#         elif race_type == 'lap':
#             lap_based_fuel()
#             break
#         elif race_type == 'quit':
#             break
#         else:
#             print('Please enter timed, lap, or quit.')
#         quit


#* New master executable
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