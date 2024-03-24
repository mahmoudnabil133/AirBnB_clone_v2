#!/usr/bin/env python3
from models import *
if __name__ == '__main__':
    # st1 = State(name="kalifornia")
    # st2 = State(name="united state")
    # st1.save()
    # st2.save()
    # ct1 = City(state_id = st1.id, name="bassion")
    # ct2 = City(state_id = st1.id, name="nagrig")
    # ct3 = City(state_id = st2.id, name="san")
    # ct4 = City(state_id = st2.id, name="newyourk")
    # ct1.save()
    # ct2.save()
    # ct3.save()
    # ct4.save()
    # print("")
    all_states = storage.all(State)
    for state_id, state in all_states.items():
        for city in state.cities:
            print("Find the city {} in the state {}".format(city.name, state.name))
