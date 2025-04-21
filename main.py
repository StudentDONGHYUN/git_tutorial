from utils import load_characters
from player import Character

def main():
    chars = load_characters('characters.ini')
    print("사용 가능한 캐릭터:")
    for name in chars:
        print(f" - {name}")
    sel = input("캐릭터명을 입력하세요: ")
    stats = chars.get(sel)
    if not stats:
        print("잘못된 캐릭터명")
        return

    player = Character(sel, stats['basic'], stats['skills'])
    moves = {'w':'위쪽', 'a':'왼쪽', 's':'아래쪽', 'd':'오른쪽'}

    print("조작법: w/a/s/d 이동, b 기본공격, 1~5 스킬, q 종료")
    while True:
        key = input("키 입력: ").strip()
        if key == 'q':
            print("게임 종료")
            break
        if key in moves:
            print(f"{moves[key]} 이동")
            continue
        if key == 'b':
            dmg = player.attack()
            print(f"기본 공격! 데미지 {dmg}")
            continue
        if key in ['1','2','3','4','5']:
            lvl = int(key)
            dmg = player.use_skill(lvl)
            print(f"{lvl}차 스킬! 데미지 {dmg}")
            continue
        print("알 수 없는 입력")
        
if __name__ == "__main__":
    main()