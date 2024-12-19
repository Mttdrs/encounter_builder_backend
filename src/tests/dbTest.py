from src.entities.actors.actor import Actor

actorDictionary = {
    "id": 0,
    "name": 'TestName',
    "description": 'TestDesc',
    "armorClass": 10,
    "hitPoints": 10,
    "averageSave": 0.0,
    "toHitBonus": 0,
    "saveDC": 0,
    "baseDPR": 0.0,
    "maxDpr": 0.0
}

test = Actor.fromDictionary(actorDictionary)
Actor.insertActorDirect(test)
 
print(test.name)