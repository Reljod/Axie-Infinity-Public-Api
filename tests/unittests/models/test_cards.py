from api.models.cards import CardFilterBasic, Card, CardList, AxieType, CardAttackType
import pytest


test_sample = CardList(cards=[
    Card(
        part_name="part_name1",
        card_name="card_name1",
        card_class=AxieType.BUG,
        attack=100,
        shield=100,
        attack_type=CardAttackType.MELEE
    ),
    Card(
        part_name="part_name2",
        card_name="card_name2",
        card_class=AxieType.AQUA,
        attack=100,
        shield=100,
        attack_type=CardAttackType.RANGE
    ),
    Card(
        part_name="part_name3",
        card_name="card_name3",
        card_class=AxieType.AQUA,
        attack=20,
        shield=0,
        attack_type=CardAttackType.RANGE
    ),
])

def test_is_part_name_filter_returning_correctly():
    filter_basic = CardFilterBasic(part_name="part_name3")
    card_list = filter_basic.filter(test_sample.copy())  # Copying is needed to so that the
    # test sample in the next tests won't break since the test_sample is mutable.
    
    assert card_list == CardList(cards=[
        Card(
            part_name="part_name3",
            card_name="card_name3",
            card_class=AxieType.AQUA,
            attack=20,
            shield=0,
            attack_type=CardAttackType.RANGE
        )
    ])
    
def test_is_card_name_filter_returning_correctly():
    filter_basic = CardFilterBasic(card_name="card_name2")
    card_list = filter_basic.filter(test_sample.copy())
    
    assert card_list == CardList(cards=[
        Card(
            part_name="part_name2",
            card_name="card_name2",
            card_class=AxieType.AQUA,
            attack=100,
            shield=100,
            attack_type=CardAttackType.RANGE
        )
    ])
        
        
