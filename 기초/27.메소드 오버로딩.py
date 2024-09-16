
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print(f'{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]')

class AttackUnit(Unit): 
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name,speed,hp)
        self.damage = damage
    
    def attack(self,location):
        print(f'{self.name} : {location} 방향으로 공격합니다. 공격력 : {self.damage}')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp}입니다')
        if self.hp <= 0:
            print(f'{self.name}, 파괴되었습니다')  

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f"{name}, : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp,0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self,location):
        print('[공중 유닛 이동]')
        self.fly(self.name,location)


# 벌처 : 지상
vulture = AttackUnit('벌처',80,10,20)

#배틀크루저 : 공중
battlecruiser = FlyableAttackUnit('배틀크루저',500,25,3)

vulture.move('11시')
battlecruiser.move('9시')

