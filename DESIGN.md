# Design

The API design of Axie Infinity Public API will be around providing users information
about anything related to Axie Infinity. It will be, but not limited, to the following:
* Arena Info
* Card Stats
* Axie Stats
* Axie Adventure Stats

## Arena Info

## Card Stats
- /cards
- /cards?class=reptile&parts=back
- /card?name=XXX&other-name=XXX

### Schema
```json
{
    "cards": ["CardObject"],
    "CardObject": {
        "card-class": "aqua",
        "part-name": "blue moon",
        "card-name": "scale dart",
        "attack": 120,
        "shield": 30,
        "attack-type": "melee",
        "card-effect": "Draw a card if target is in Last Stand."
    }
}
```

## Axie Stats

## Axie Adventure Stats


