from pickletools import string1
import sqlite3
from turtle import Turtle
from fastapi import *


def my_regist(pokemon_name: str):
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()
    c.execute("insert into My_pokemon values(null,?)", [pokemon_name])
    conn.commit()
    conn.close()
    return 0
