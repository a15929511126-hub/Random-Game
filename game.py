import json
import os
import random


SAVE_FILE = "save.json"


# =========================
# 基础工具
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\n按回车继续...")


def save_game(game):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(game, f, ensure_ascii=False, indent=2)


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def new_game():
    return {
        "day": 1,
        "hp": 10,
        "mood": 70,
        "money": 50,
        "luck": 50,
        "chaos": 0,
        "flags": [],
        "achievements": [],
    }


# =========================
# 状态
# =========================

def show_status(game):
    print("=" * 36)
    print(f"第 {game['day']} 天")
    print()
    print(f"❤️  生命：{game['hp']}")
    print(f"🧠 心情：{game['mood']}")
    print(f"💰 金钱：{game['money']}")
    print(f"🍀 幸运：{game['luck']}")
    print(f"🌪️ 混乱：{game['chaos']}")
    print("=" * 36)


def change_stat(game, hp=0, mood=0, money=0, luck=0, chaos=0):
    game["hp"] += hp
    game["mood"] += mood
    game["money"] += money
    game["luck"] += luck
    game["chaos"] += chaos

    game["hp"] = max(0, min(10, game["hp"]))
    game["mood"] = max(0, min(100, game["mood"]))
    game["luck"] = max(0, min(100, game["luck"]))
    game["chaos"] = max(0, min(100, game["chaos"]))
    game["money"] = max(0, game["money"])


def add_flag(game, flag):
    if flag not in game["flags"]:
        game["flags"].append(flag)


def has_flag(game, flag):
    return flag in game["flags"]


# =========================
# 成就
# =========================

def achievement(game, name):
    if name not in game["achievements"]:
        game["achievements"].append(name)
        print()
        print("★ 获得成就！")
        print(f"  【{name}】")


def check_achievements(game):
    if game["money"] >= 200:
        achievement(game, "突然有钱")

    if game["chaos"] >= 50:
        achievement(game, "你为什么要这样做")

    if has_flag(game, "duck_friend"):
        achievement(game, "鸭子之友")

    if has_flag(game, "shoe_respected"):
        achievement(game, "鞋子是无辜的")

    if has_flag(game, "shook_duck_hand"):
        achievement(game, "和鸭子握手")

    if game["day"] >= 10 and game["chaos"] < 10:
        achievement(game, "正常人")


# =========================
# 事件：鸭子
# =========================

def duck_event(game):
    clear()

    print("你走在路上。")
    print()
    print("然后。")
    print()
    print("你看见了一只鸭子。")
    print()
    print("它站在路中间。")
    print("它也在看着你。")
    print()

    print("1. 绕开它")
    print("2. 给它一点吃的")
    print("3. 问它叫什么")
    print("4. 和它握手")

    choice = input("\n你的选择：").strip()

    if choice == "1":
        print("\n你绕开了鸭子。")
        print("鸭子没有阻止你。")
        print("这是今天最正常的事情。")

    elif choice == "2":
        print("\n你给了鸭子一点吃的。")
        print("鸭子吃掉了。")
        print("然后它跟着你走了几步。")

        change_stat(game, mood=5, chaos=3)
        add_flag(game, "duck_friend")

    elif choice == "3":
        print("\n你蹲下来。")
        print("你问：")
        print("“你叫什么？”")
        print()
        print("鸭子：")
        print("“嘎。”")
        print()
        print("你觉得这个名字挺有个性的。")

        change_stat(game, mood=3, chaos=5)
        add_flag(game, "asked_duck_name")

    elif choice == "4":
        print("\n你伸出了手。")
        print()
        print("鸭子看了看你的手。")
        print("又看了看你。")
        print()
        print("它居然真的把翅膀递了过来。")
        print()
        print("你们握手了。")

        change_stat(game, mood=10, chaos=10)
        add_flag(game, "shook_duck_hand")

    else:
        print("\n你什么也没做。")
        print("鸭子似乎有点失望。")

    pause()


# =========================
# 事件：神秘鞋子
# =========================

def shoe_event(game):
    clear()

    print("你在路边发现了一只鞋。")
    print()
    print("是一只非常普通的鞋。")
    print()
    print("但不知道为什么。")
    print()
    print("你觉得它在看着你。")
    print()

    print("1. 无视它")
    print("2. 把鞋摆正")
    print("3. 对鞋说你好")
    print("4. 把鞋带走")

    choice = input("\n你的选择：").strip()

    if choice == "1":
        print("\n你决定不管它。")
        print("这是一个非常理智的决定。")

    elif choice == "2":
        print("\n你把鞋摆正了。")
        print()
        print("不知道为什么。")
        print("你感觉世界变得正常了一点。")

        change_stat(game, mood=3, chaos=-3)
        add_flag(game, "shoe_respected")

    elif choice == "3":
        print("\n你说：")
        print("“你好。”")
        print()
        print("鞋没有回答。")
        print()
        print("但你觉得它听见了。")

        change_stat(game, mood=2, chaos=5)
        add_flag(game, "talked_to_shoe")

    elif choice == "4":
        print("\n你把鞋捡走了。")
        print()
        print("你现在拥有：")
        print("【一只不知道有什么用的鞋】")

        change_stat(game, mood=5, chaos=12)
        add_flag(game, "stole_shoe")

    else:
        print("\n你站在鞋面前。")
        print("什么也没做。")

    pause()


# =========================
# 事件：自动售货机
# =========================

def vending_event(game):
    clear()

    print("你发现了一台自动售货机。")
    print()
    print("上面只有一个按钮。")
    print()
    print("按钮写着：")
    print()
    print("【不要按】")
    print()

    print("1. 不按")
    print("2. 按一下")
    print("3. 连续按十次")

    choice = input("\n你的选择：").strip()

    if choice == "1":
        print("\n你忍住了。")
        print("你成功地没有按一个明显不该按的按钮。")
        change_stat(game, mood=2, chaos=-2)

    elif choice == "2":
        print("\n你按了一下。")
        print()
        print("咔哒。")
        print()
        print("售货机掉出来一瓶水。")
        print()
        print("你获得了：水。")
        change_stat(game, mood=3, chaos=5)

    elif choice == "3":
        print("\n你疯狂地按了十次。")
        print()
        print("售货机开始震动。")
        print()
        print("然后……")
        print()
        print("吐出来 50 元。")
        print()
        print("你决定今天不再思考这件事。")

        change_stat(game, money=50, mood=10, chaos=15)
        add_flag(game, "vending_machine")

    else:
        print("\n你看着按钮。")
        print("按钮也看着你。")

    pause()


# =========================
# 事件：银行
# =========================

def bank_event(game):
    clear()

    print("你打开手机。")
    print()
    print("银行 APP 显示：")
    print()
    print("余额：")
    print(f"¥ {game['money']}")
    print()
    print("你确认了一遍。")
    print()
    print("余额：")
    print(f"¥ {game['money']}")
    print()
    print("突然，你的账户多了 20 元。")
    print()
    print("备注：")
    print("“谢谢。”")

    change_stat(game, money=20, mood=8, chaos=8)
    add_flag(game, "mysterious_money")

    pause()


# =========================
# 事件：星期六上班
# =========================

def work_event(game):
    clear()

    print("今天是星期六。")
    print()
    print("你睁开眼。")
    print()
    print("手机上有一条消息：")
    print()
    print("【今天记得上班。】")
    print()
    print("你沉默了。")
    print()
    print("你确认了一遍日期。")
    print()
    print("确实是星期六。")

    print()
    print("1. 去上班")
    print("2. 装死")
    print("3. 回复：我已经死了")

    choice = input("\n你的选择：").strip()

    if choice == "1":
        print("\n你去上班了。")
        print("老板夸你很有责任心。")
        print("然后给了你 10 元。")

        change_stat(game, money=10, mood=-5, chaos=3)

    elif choice == "2":
        print("\n你把手机倒扣。")
        print("世界安静了。")

        change_stat(game, mood=8, chaos=5)

    elif choice == "3":
        print("\n你回复：")
        print("“我已经死了。”")
        print()
        print("对方回复：")
        print("“那明天来加班。”")

        change_stat(game, mood=-10, chaos=10)

    else:
        print("\n你决定假装没有看到。")

    pause()


# =========================
# 随机事件
# =========================

def normal_event(game):
    events = [
        duck_event,
        shoe_event,
        vending_event,
        bank_event,
        work_event,
    ]

    event = random.choice(events)
    event(game)


# =========================
# 高混乱事件
# =========================

def chaos_event(game):
    clear()

    print("空气突然安静了。")
    print()
    print("你感觉有什么东西不太对。")
    print()
    print("然后你发现……")
    print()
    print("所有路人都在看着你。")
    print()
    print("一个路人走过来。")
    print()
    print("他说：")
    print("“你是不是已经发现了？”")
    print()

    print("1. 发现什么？")
    print("2. 我什么都不知道")
    print("3. 是的")

    choice = input("\n你的选择：").strip()

    if choice == "1":
        print("\n路人点了点头。")
        print("“果然。”")
        print()
        print("然后他转身走了。")

        change_stat(game, mood=-3, chaos=10)

    elif choice == "2":
        print("\n路人盯着你。")
        print()
        print("“很好。”")
        print()
        print("“继续保持。”")

        change_stat(game, chaos=5)

    elif choice == "3":
        print("\n你点头。")
        print()
        print("路人也点头。")
        print()
        print("你们谁都没有解释。")
        print()
        print("但你知道。")
        print("事情开始变得奇怪了。")

        change_stat(game, mood=5, chaos=20)
        add_flag(game, "knows_too_much")

    pause()


# =========================
# 特殊事件
# =========================

def special_event(game):
    if has_flag(game, "duck_friend") and has_flag(game, "shoe_respected"):
        clear()

        print("你今天出门的时候。")
        print()
        print("发现门口放着一只鞋。")
        print()
        print("鞋里面站着一只鸭子。")
        print()
        print("你沉默了。")
        print()
        print("鸭子也沉默了。")
        print()
        print("你们似乎都知道事情已经无法挽回。")

        change_stat(game, mood=15, chaos=20)
        add_flag(game, "duck_shoe_meeting")

        pause()
        return True

    return False


# =========================
# 每日流程
# =========================

def play_day(game):
    clear()

    print(f"第 {game['day']} 天")
    print()
    print("你醒了。")
    print()
    print("今天应该也不会发生什么大事。")
    print()

    pause()

    if special_event(game):
        return

    if game["chaos"] >= 60:
        chaos_event(game)
    else:
        normal_event(game)


# =========================
# 游戏结束
# =========================

def game_over(game):
    clear()

    print("=" * 36)
    print("游戏结束")
    print("=" * 36)
    print()

    if game["hp"] <= 0:
        print("你的生命值归零了。")
        print("看来今天确实出了大问题。")
    elif game["mood"] <= 0:
        print("你的心情归零了。")
        print("你决定躺平。")
    else:
        print("世界线发生了某些不可描述的变化。")

    print()
    print(f"你活到了第 {game['day']} 天。")
    print(f"最终金钱：{game['money']}")
    print(f"最终混乱：{game['chaos']}")

    check_achievements(game)

    print()
    print("获得的成就：")

    if game["achievements"]:
        for item in game["achievements"]:
            print(f"  ★ {item}")
    else:
        print("  ……一个都没有。")

    save_game(game)

    pause()


# =========================
# 帮助
# =========================

def instructions():
    clear()

    print("=" * 36)
    print("《今天也没出大问题》")
    print("=" * 36)
    print()
    print("这是一个非常认真的小游戏。")
    print()
    print("你每天都会遇到一些事情。")
    print()
    print("有些事情很正常。")
    print("有些事情不太正常。")
    print("还有一些事情……")
    print("最好不要问为什么。")
    print()
    print("你的选择会影响：")
    print("❤️ 生命")
    print("🧠 心情")
    print("💰 金钱")
    print("🍀 幸运")
    print("🌪️ 混乱")
    print()
    print("世界会记住你做过的事情。")
    print()
    print("游戏会自动保存。")
    print("存档文件是 save.json。")
    print()
    print("如果想重新开始，")
    print("可以在主菜单选择删除存档。")

    pause()


# =========================
# 主菜单
# =========================

def main_menu():
    while True:
        clear()

        print("=" * 36)
        print("      今天也没出大问题")
        print("=" * 36)
        print()
        print("1. 开始游戏")
        print("2. 游戏说明")
        print("3. 查看成就")
        print("4. 删除存档")
        print("5. 退出")
        print()

        choice = input("请选择：").strip()

        if choice == "1":
            game = load_game()

            if game is None:
                game = new_game()

            game_loop(game)

        elif choice == "2":
            instructions()

        elif choice == "3":
            game = load_game()

            clear()
            print("成就")
            print("=" * 36)
            print()

            if game and game["achievements"]:
                for item in game["achievements"]:
                    print(f"★ {item}")
            else:
                print("还没有获得任何成就。")
                print()
                print("去遇到一只鸭子吧。")

            pause()

        elif choice == "4":
            if os.path.exists(SAVE_FILE):
                print()
                confirm = input("确定删除存档吗？(y/n)：").strip().lower()

                if confirm == "y":
                    os.remove(SAVE_FILE)
                    print("存档已删除。")
                    pause()
            else:
                print()
                print("目前没有存档。")
                pause()

        elif choice == "5":
            print()
            print("再见。")
            break

        else:
            print()
            print("没有这个选项。")
            pause()


# =========================
# 游戏主循环
# =========================

def game_loop(game):
    while True:
        if game["hp"] <= 0 or game["mood"] <= 0:
            game_over(game)
            return

        clear()
        show_status(game)

        print()
        print("1. 开始今天")
        print("2. 查看状态")
        print("3. 保存游戏")
        print("4. 返回主菜单")
        print()

        choice = input("请选择：").strip()

        if choice == "1":
            play_day(game)

            check_achievements(game)

            game["day"] += 1

            # 幸运会随着时间轻微变化
            game["luck"] = max(
                0,
                min(
                    100,
                    game["luck"] + random.randint(-5, 5)
                )
            )

            save_game(game)

        elif choice == "2":
            clear()
            show_status(game)

            print()
            if game["flags"]:
                print("世界记住的事情：")
                for flag in game["flags"]:
                    print(f"  - {flag}")
            else:
                print("目前还没有特别的事情发生。")

            pause()

        elif choice == "3":
            save_game(game)
            print()
            print("保存成功。")
            pause()

        elif choice == "4":
            save_game(game)
            return

        else:
            print()
            print("没有这个选项。")
            pause()


if __name__ == "__main__":
    main_menu()
