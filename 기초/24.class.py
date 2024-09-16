class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성 되었습니다')
        print(f'체력 : {self.hp}, 공격력 : {damage}')

marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = Unit('레이스', 80, 5)
print(f'유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}')
# 외부에서 멤버 변수 사용 가능

# 마인드 컨트롤 : 상대유닛을 뻇음
wraith2 = Unit('뺴앗은 레이스', 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print(f'{wraith2.name}는 현재 클로킹 상태입니다')
