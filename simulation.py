import numpy as np
import pandas as pd
def simulate_game():
    # Create 3 doors, one randomly containing a car and the other two containing goats
    door_list = ['rand1', 'rand2', 'rand3']
    door_list[door_list.index(np.random.choice(door_list))] = 'car'
    for i in range(len(door_list)):
        if door_list[i] != 'car':
            door_list[i] = 'goat'
    # Assume initially that the choice is made at random
    choice_initial = np.random.choice(door_list)
    # Host opens (removes) one goat
    door_list.remove('goat')
    # When given option: CHANGE
    # We know that the two doors left include 1 goat and 1 car
    final_choice_change = ''
    if choice_initial == 'goat':
        choice_change = 'car'
    else:
        choice_change = 'goat'
    # When given option: DONT CHANGE
    choice_nochange = choice_initial
    # Return binary success integers (1=win, 0=lose)
    return [(choice_change=='car')*1, (choice_nochange=='car')*1]
df = pd.DataFrame(columns=['Change', 'Dont Change'])
for i in range(10000):
    df.loc[len(df)] = simulate_game()
print(df.mean())
