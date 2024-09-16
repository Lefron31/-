

def checkpoint(soldiers,gun):
    # global gun # 전역 공간에 있는 gun 사용
    gun=gun - soldiers
    print(f'함수 내 남은 총 : {gun}')
    return gun

print(f'전체 총 : {checkpoint(2,10)}')