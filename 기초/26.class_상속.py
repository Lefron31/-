# 일반 유닛
class Unit:             # 부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#unit과 attacktunit 내 겹치는 인자 name, hp


class AttackUnit(Unit):         # 자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name,hp) # 다른 클래스에서 값을 가져옴
        self.damage = damage
    
    def attack(self,location):
        print(f'{self.name} : {location} 방향으로 공격합니다. 공격력 : {self.damage}')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp}입니다')
        if self.hp <= 0:
            print(f'{self.name}, 파괴되었습니다')

# 파이어뱃 : 공격
firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시')
firebat1.damaged(25)
firebat1.damaged(25)

# 드랍쉽 : 날수있음 / 공격 x

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f"{name}, : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")
    

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, damage)
        Flyable.__init__(self, flying_speed)

#발키리 : 공중