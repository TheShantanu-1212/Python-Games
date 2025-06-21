import pandas

states_data = pandas.read_csv("50_states.csv")
num_states = len(states_data)
states_names = states_data["state"]
for name in states_names:
    print(name)