import random  

from hero import Hero
from power import Power
from heroes_power import HeroPower
from app import app
from config import db

app.app_context().push()

powers = [
    {'name': 'super strength', 'description': 'gives the wielder super-human strengths'},
    {'name': 'flight', 'description': 'gives the wielder the ability to fly through the skies at supersonic speed'},
    {'name': 'super human senses', 'description': 'allows the wielder to use her senses at a super-human level'},
    {'name': 'elasticity', 'description': 'can stretch the human body to extreme lengths'}
]

for power_data in powers:
    power = Power(**power_data)
    db.session.add(power)

heroes = [
    {'name': 'Kamala Khan', 'super_name': 'Ms. Marvel'},
    {'name': 'Doreen Green', 'super_name': 'Squirrel Girl'},
    {'name': 'Gwen Stacy', 'super_name': 'Spider-Gwen'},
    {'name': 'Janet Van Dyne', 'super_name': 'The Wasp'},
    {'name': 'Wanda Maximoff', 'super_name': 'Scarlet Witch'},
    {'name': 'Carol Danvers', 'super_name': 'Captain Marvel'},
    {'name': 'Jean Grey', 'super_name': 'Dark Phoenix'},
    {'name': 'Ororo Munroe', 'super_name': 'Storm'},
    {'name': 'Kitty Pryde', 'super_name': 'Shadowcat'},
    {'name': 'Elektra Natchios', 'super_name': 'Elektra'}
]

for hero_data in heroes:
    hero = Hero(**hero_data)
    db.session.add(hero)

db.session.commit()

strengths = ['Strong', 'Weak', 'Average']

for hero in Hero.query.all():
    for _ in range(1, 4):
        power = random.choice(Power.query.all())
        strength = random.choice(strengths)

        hero_power = HeroPower(hero=hero, power=power, strength=strength)
        db.session.add(hero_power)

db.session.commit()

print('🦸‍♀️ Seeding complete!')
