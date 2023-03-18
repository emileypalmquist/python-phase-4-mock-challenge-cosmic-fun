#!/usr/bin/env python3

from random import choice as rc, randint

from faker import Faker

from app import app
from models import db, Mission, Planet, Scientist

fake = Faker()

scientist_names = [{"name": "John M. Grunsfeld", "field_of_study": "Physics", "avatar": "http://t2.gstatic.com/licensed-image?q=tbn:ANd9GcScR8jJkcRs1jwAMOQNLJHfLF63yFX12gPMImUFf_7657RCGpk9H-JzI_EFsgzb85vG"}, {"name": "Kathryn D. Sullivan", "field_of_study": "Geology", "avatar": "http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTvBnpKEY3f22XIRw-R-PQgEPKW5WwZIU26r4srUo9ps8QnvziV-8M5YHR_FiJDuUmv"},
                   {"name": "Jessica Watkins", "field_of_study": "Geologist", "avatar": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Jessica_Watkins_Official_NASA_Portrait_in_2021_%28cropped%29.jpg"}, {
                       "name": "Josh A. Cassada", "field_of_study": "Physics", "avatar": "http://t2.gstatic.com/licensed-image?q=tbn:ANd9GcQtZW2qff5cNijHDMWOqVQljN8OQn-J7OURnrSWGhEhPOpm9VG3doOBJzHFnRWjvYpX"},
                   {"name": "Maggie Aderin-Pocock", "field_of_study": "Physics", "avatar": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTaAMxB1wogeYWozIk8hLGr8JbNWAhQhHZKuOtBbYO482AMAeNO"}, {
                       "name": "Karl Gordon Henize", "field_of_study": "Astronomy", "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Henize.jpg/1200px-Henize.jpg"},
                   {"name": "Joseph M Acaba", "field_of_study": "Hydrogeology", "avatar": "http://t1.gstatic.com/licensed-image?q=tbn:ANd9GcTzDn9v_9ITBP-nOTIJwGvrQttCJBiuspb5vXRKwJfG19bO198mZRQPlvnDll0kZeJY"}, {"name": "Sally Ride", "field_of_study": "Physics", "avatar": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmImcTrOawh1PJyqSDw3fh-GfZfozJ2w9E_jU7B3m3CDC4tDPU"}]


def make_scientists():

    Scientist.query.delete()

    scientists = []

    for scientist_dict in scientist_names:
        scientist = Scientist(
            name=scientist_dict["name"],
            field_of_study=scientist_dict["field_of_study"],
            avatar=scientist_dict["avatar"]
        )
        scientists.append(scientist)

    db.session.add_all(scientists)
    db.session.commit()


planets_list = [
    {"name": "Mercury", "image": "https://nineplanets.org/wp-content/uploads/2019/09/mercury.png"},
    {"name": "Venus", "image": "https://nineplanets.org/wp-content/uploads/2019/09/venus.png"},
    {"name": "Mars", "image": "https://nineplanets.org/wp-content/uploads/2019/09/mars.png"},
    {"name": "Jupitor", "image": "https://nineplanets.org/wp-content/uploads/2019/09/jupiter.png"},
    {"name": "Saturn", "image": "https://nineplanets.org/wp-content/uploads/2019/09/saturn.png"},
    {"name": "Uranus", "image": "https://nineplanets.org/wp-content/uploads/2019/09/uranus.png"},
    {"name": "Neptune", "image": "https://nineplanets.org/wp-content/uploads/2019/09/neptune.png"},
]
stars_list = ["Sirius", "Antares", "Betelgeuse",
              "Iota Draconis", "Theta Lionis", "Hamal"]


def make_planets():

    Planet.query.delete()

    planets = []

    for planet_dict in planets_list:
        planet = Planet(
            name=planet_dict["name"],
            distance_from_earth=randint(1, 10),
            nearest_star=rc(stars_list),
            image=planet_dict["image"]
        )
        planets.append(planet)

    db.session.add_all(planets)
    db.session.commit()


def make_missions():

    Mission.query.delete()
    planets = Planet.query.with_entities(Planet.id).all()
    scientists = Scientist.query.with_entities(Scientist.id).all()

    missions = []

    for i in range(20):
        mission = Mission(
            name=fake.slug(),
            scientist_id=rc(scientists)[0],
            planet_id=rc(planets)[0]
        )
        missions.append(mission)

    db.session.add_all(missions)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        make_scientists()
        make_planets()
        make_missions()
