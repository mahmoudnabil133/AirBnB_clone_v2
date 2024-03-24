#!/usr/bin/env python3

from os import getenv
from os import getenv
import models
from models.city import City
from models.base_model import Base, BaseModel
from models.base_model import Column, relationship, String
from models.state import State

type = getenv('HBNB_TYPE_STORAGE')
if __name__ == '__main__':
    st1 = State(name="kalifornia")
    st2 = State(name="united state")
    st1.save()
    st2.save()
    ct1 = City(state_id = st1.id, name="bassion")
    ct2 = City(state_id = st1.id, name="nagrig")
    ct3 = City(state_id = st2.id, name="san")
    ct4 = City(state_id = st2.id, name="newyourk")
    ct1.save()
    ct2.save()
    ct3.save()
    ct4.save()
    print("")
    all_states = models.storage.all(State)
    for state_id, state in all_states.items():
        for city in state.cities:
            print("Find the city {} in the state {}".format(city.name, state.name))
