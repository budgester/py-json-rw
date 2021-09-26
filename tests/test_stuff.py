import os
from app.app import Stuff

def test_stuff():
    data = [{'a': 1},{'b': 2}]
    s = Stuff(data)

def test_stuff_display_data():
    data = [{'a': 1}, {'b': 2}]
    s = Stuff(data).display_data()
    assert len(s) == 2

def test_add_data():
    data = [{'a': 1,},{'b': 2}]
    s = Stuff(data)
    s.add_data({"c":3})
    assert 3 == len(s.data)

def test_load_json():
    s = Stuff()
    s.load_json()
    assert 3 == len(s.data)

def test_save_json():
    json_file = "data_new.json"
    if os.path.exists(json_file):
        os.remove(json_file)
    s = Stuff()
    s.load_json()
    s.add_data({"z":99})
    s.save_json()
    assert 4 == len(s.data)
    assert os.path.exists(json_file)