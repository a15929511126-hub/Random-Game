import json
import os

SAVE_FILE = "save.json"


def default_game():
    return {
        "day": 1,
        "hp": 100,
        "mood": 70,
        "money": 100,
        "luck": 50,
        "chaos": 0,

        "memory": {
            "duck_met": False,
            "duck_fed": False,
            "duck_named": False,
            "duck_handshake": False,

            "vending_pressed": 0,
            "vending_observed": False,

            "shoe_found": False,
            "shoe_upright": False,
            "shoe_greeted": False,
            "shoe_taken": False,

            "money_received": 0,
            "money_investigated": False,
            "money_spent": False,

            "went_to_work": False,
            "pretended_dead": False,
            "said_saturday": False
        },

        "history": [],
        "finished": False
    }


def load_game():
    if not os.path.exists(SAVE_FILE):
        return default_game()

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default_game()


def save_game(game):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(game, f, ensure_ascii=False, indent=2)


def say(text):
    print()
    print(text)


def choose(options):
    print()
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        answer = input("\n> ").strip()

        if answer.isdigit():
            number = int(answer)

            if 1 <= number <= len(options):
                return number

        print("请输入一个有效的选项。")


def change(game, stat, amount):
    game[stat] += amount


# --------------------------------------------------
# DAY 1
# --------------------------------------------------

def day_one(game):
    say("星期一。")
    say("你醒了。")
    say("今天看起来和平时没有什么区别。")

    say("走到路口的时候，你看到一只鸭子。")
    say("它站在路中间。")
    say("它看起来完全没有打算让路。")

    choice = choose([
        "绕过它",
        "给它一点食物",
        "问它叫什么名字",
        "和它握手"
    ])

    game["memory"]["duck_met"] = True

    if choice == 1:
        say("你绕开了鸭子。")
        say("鸭子看了你一眼。")
        game["history"].append("绕过了鸭子")

    elif choice == 2:
        say("你给了鸭子一点食物。")
        say("它吃掉了。")
        say("然后看了你很久。")
        game["memory"]["duck_fed"] = True
        game["mood"] += 5
        game["history"].append("给鸭子喂了食物")

    elif choice == 3:
        say("你问它叫什么名字。")
        say("鸭子看着你。")
        say("……嘎。")
        game["memory"]["duck_named"] = True
        game["chaos"] += 2
        game["history"].append("问鸭子叫什么名字")

    elif choice == 4:
        say("你伸出了手。")
        say("鸭子也伸出了翅膀。")
        say("你们握了握手。")
        say("……")
        say("这应该算正常吧。")
        game["memory"]["duck_handshake"] = True
        game["chaos"] += 10
        game["luck"] += 5
        game["history"].append("和鸭子握了手")


# --------------------------------------------------
# DAY 2
# --------------------------------------------------

def day_two(game):
    say("星期二。")
    say("你在回家的路上发现了一台自动售货机。")

    say("它只有一个按钮。")
    say("按钮上写着：")
    say("“不要按。”")

    if game["memory"]["duck_met"]:
        say("售货机旁边好像有什么东西动了一下。")

    choice = choose([
        "离开",
        "按一次",
        "连续按十次",
        "仔细观察售货机"
    ])

    if choice == 1:
        say("你决定不碰它。")
        game["history"].append("没有按售货机")

    elif choice == 2:
        say("你按了一次。")
        say("售货机沉默了三秒。")
        say("然后掉出来一瓶饮料。")
        game["money"] += 5
        game["memory"]["vending_pressed"] = 1
        game["chaos"] += 5
        game["history"].append("按了一次售货机")

    elif choice == 3:
        say("你连续按了十次。")
        say("售货机开始震动。")
        say("然后屏幕上出现了一句话：")
        say("“真的不要按。”")
        game["money"] += 30
        game["memory"]["vending_pressed"] = 10
        game["chaos"] += 20
        game["history"].append("连续按了十次售货机")

    elif choice == 4:
        say("你没有按。")
        say("你观察了一会儿。")
        say("售货机的屏幕突然亮了一下。")
        say("“谢谢。”")
        game["memory"]["vending_observed"] = True
        game["chaos"] += 3
        game["history"].append("观察了售货机")


# --------------------------------------------------
# DAY 3
# --------------------------------------------------

def day_three(game):
    say("星期三。")
    say("今天下雨了。")

    say("你在路边发现了一只鞋。")
    say("只有一只。")
    say("它看起来非常普通。")

    say("但是鞋尖正对着你。")

    choice = choose([
        "无视它",
        "把鞋摆正",
        "和鞋打个招呼",
        "把鞋捡起来"
    ])

    game["memory"]["shoe_found"] = True

    if choice == 1:
        say("你没有理会它。")
        game["history"].append("无视了鞋")

    elif choice == 2:
        say("你把鞋摆正了。")
        say("这样看起来舒服多了。")
        game["memory"]["shoe_upright"] = True
        game["history"].append("把鞋摆正")

    elif choice == 3:
        say("你对鞋说了一声：“你好。”")
        say("雨声里没有任何回应。")
        say("至少暂时没有。")
        game["memory"]["shoe_greeted"] = True
        game["chaos"] += 5
        game["history"].append("和鞋打招呼")

    elif choice == 4:
        say("你把鞋捡了起来。")
        say("它比看起来稍微重一点。")
        game["memory"]["shoe_taken"] = True
        game["chaos"] += 10
        game["history"].append("捡起了鞋")


# --------------------------------------------------
# DAY 4
# --------------------------------------------------

def day_four(game):
    say("星期四。")

    say("你打开银行账户。")

    say("余额：")

    game["money"] += 20
    game["memory"]["money_received"] += 20

    say(f"{game['money']} 元。")

    say("你很确定昨天不是这个数字。")

    say("转账备注只有两个字：")
    say("“谢谢。”")

    choice = choose([
        "把钱花掉",
        "存着",
        "调查钱从哪里来的",
        "假装没看见"
    ])

    if choice == 1:
        say("你决定把这笔钱花掉。")
        game["money"] = max(0, game["money"] - 20)
        game["memory"]["money_spent"] = True
        game["chaos"] += 5
        game["history"].append("花掉了神秘转账")

    elif choice == 2:
        say("你决定先存着。")
        game["history"].append("保存了神秘转账")

    elif choice == 3:
        say("你开始调查。")
        say("没有找到任何转账记录。")
        say("但你发现备注似乎变成了：")
        say("“还差一点。”")
        game["memory"]["money_investigated"] = True
        game["chaos"] += 8
        game["history"].append("调查神秘转账")

    elif choice == 4:
        say("你决定当作没看见。")
        say("但你总觉得有人知道你看见了。")
        game["history"].append("假装没看见神秘转账")


# --------------------------------------------------
# DAY 5
# --------------------------------------------------

def day_five(game):
    say("星期五。")

    say("你的手机收到一条消息。")

    say("“今天记得上班。”")

    say("你看了一眼日历。")
    say("星期六。")

    choice = choose([
        "去上班",
        "装死",
        "回复：我已经死了",
        "回复：今天星期六"
    ])

    if choice == 1:
        say("你还是去了。")
        say("公司里没有一个人觉得奇怪。")
        game["memory"]["went_to_work"] = True
        game["mood"] -= 5
        game["history"].append("星期六去上班")

    elif choice == 2:
        say("你决定装死。")
        say("世界暂时没有发现。")
        game["chaos"] += 5
        game["history"].append("星期六装死")

    elif choice == 3:
        say("你回复：")
        say("“我已经死了。”")
        say("对方很快回复：")
        say("“那明天来加班。”")
        game["memory"]["pretended_dead"] = True
        game["chaos"] += 15
        game["history"].append("告诉对方自己死了")

    elif choice == 4:
        say("你回复：")
        say("“今天星期六。”")
        say("三分钟后。")
        say("对方回复：")
        say("“知道。”")
        game["memory"]["said_saturday"] = True
        game["chaos"] += 10
        game["history"].append("提醒对方今天星期六")


# --------------------------------------------------
# DAY 6
# --------------------------------------------------

def day_six(game):
    say("星期六。")

    say("你在路边再次遇见那只鸭子。")

    if game["memory"]["duck_fed"]:
        say("鸭子看到你以后走了过来。")
        say("它看起来记得你。")
        say("你没有带食物。")
        say("但它还是站在你旁边。")

    elif game["memory"]["duck_handshake"]:
        say("鸭子看到你以后停了下来。")
        say("然后慢慢伸出了翅膀。")
        say("它在等你。")

        choice = choose([
            "再次握手",
            "装作没看见",
            "问它鞋去哪了"
        ])

        if choice == 1:
            say("你们再次握手。")
            game["chaos"] += 5
            game["history"].append("第二次和鸭子握手")

        elif choice == 2:
            say("你假装没看见。")
            say("鸭子似乎有点失望。")
            game["history"].append("没有回应鸭子的握手")

        else:
            say("你问：")
            say("“你的鞋去哪了？”")
            say("鸭子歪了歪头。")
            say("然后看向远处。")
            game["chaos"] += 8
            game["history"].append("问鸭子鞋去哪了")

    elif game["memory"]["duck_named"]:
        say("鸭子看到你以后叫了一声。")
        say("“嘎。”")
        say("但这次的声音听起来和上次不太一样。")

    else:
        say("鸭子看见了你。")
        say("……")
        say("然后走了。")

    game["history"].append("再次遇见鸭子")


# --------------------------------------------------
# DAY 7
# --------------------------------------------------

def day_seven(game):
    say("星期日。")
    say("你回到家。")

    memory = game["memory"]

    if memory["shoe_found"] and memory["duck_met"] and game["chaos"] < 30:

        say("门口放着一只鞋。")
        say("就是你星期三见过的那只。")

        say("鸭子站在鞋旁边。")

        say("鞋尖对着你。")
        say("鸭子也在看着你。")

        say("你突然产生了一种非常奇怪的感觉。")

        choice = choose([
            "问鸭子发生了什么",
            "捡起鞋",
            "后退几步",
            "什么都不做"
        ])

        if choice == 1:
            say("你问鸭子：")
            say("“这是怎么回事？”")
            say("鸭子看了看鞋。")
            say("然后看了看你。")
            say("“嘎。”")

        elif choice == 2:
            say("你捡起了鞋。")
            say("鸭子没有阻止你。")
            say("只是叹了口气。")
            say("……")
            say("你确定自己听见了叹气。")

        elif choice == 3:
            say("你后退了一步。")
            say("鸭子也后退了一步。")
            say("鞋没有动。")

        else:
            say("你什么都没做。")
            say("过了一会儿。")
            say("鸭子叼起鞋走了。")

        game["history"].append("发现鸭子和鞋在一起")

    elif game["chaos"] >= 30:

        say("你打开家门。")
        say("客厅里坐着一个陌生人。")

        say("他正在喝你的水。")

        say("你问：")
        say("“你是谁？”")

        say("他说：")
        say("“我负责观察。”")

        say("你沉默了一会儿。")

        say("他又说：")
        say("“你这一周过得挺热闹。”")

        say("然后他放下杯子。")

        say("“下周见。”")

        game["history"].append("见到了观察者")

    else:

        say("今天没有发生什么特别的事情。")
        say("你坐在家里。")
        say("窗外很安静。")

        if memory["vending_pressed"] > 0:
            say("手机突然响了一下。")
            say("一条陌生消息：")
            say("“今天也来啦。”")

        say("你不知道是谁发的。")


# --------------------------------------------------
# PLAYER PROFILE
# --------------------------------------------------

def show_profile(game):
    memory = game["memory"]

    say("========== 玩家档案 ==========")

    print(f"游戏天数：{game['day'] - 1}")
    print(f"最终心情：{game['mood']}")
    print(f"最终金钱：{game['money']}")
    print(f"混乱程度：{game['chaos']}")

    print()

    tendencies = []

    if memory["duck_fed"]:
        tendencies.append("善意")

    if memory["duck_named"] or memory["shoe_greeted"]:
        tendencies.append("好奇")

    if memory["vending_observed"] or memory["money_investigated"]:
        tendencies.append("谨慎")

    if memory["duck_handshake"] or memory["shoe_taken"]:
        tendencies.append("大胆")

    if game["chaos"] >= 30:
        tendencies.append("混乱")

    if not tendencies:
        tendencies.append("平静")

    print("行为倾向：")
    print(" / ".join(tendencies))

    print()
    print("你做过的事情：")

    for item in game["history"]:
        print(f"- {item}")

    print()

    if game["chaos"] >= 30:
        print("世界评价：这个 AI 很难预测。")
    elif memory["duck_fed"]:
        print("世界评价：这个 AI 看起来还不错。")
    elif memory["duck_handshake"]:
        print("世界评价：这个 AI 有点奇怪。")
    else:
        print("世界评价：这个 AI 很正常。")

    print()
    print("========== 第一周结束 ==========")


# --------------------------------------------------
# DAY SYSTEM
# --------------------------------------------------

def play_day(game):

    day = game["day"]

    say(f"========== 第 {day} 天 ==========")

    if day == 1:
        day_one(game)

    elif day == 2:
        day_two(game)

    elif day == 3:
        day_three(game)

    elif day == 4:
        day_four(game)

    elif day == 5:
        day_five(game)

    elif day == 6:
        day_six(game)

    elif day == 7:
        day_seven(game)

    game["day"] += 1

    save_game(game)

    if game["day"] > 7:
        game["finished"] = True
        save_game(game)

        show_profile(game)


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def instructions():
    print()
    print("《今天也没出大问题》")
    print()
    print("这是一个专门给 AI 玩的小世界。")
    print()
    print("没有正确答案。")
    print("世界不会告诉你哪一个选择最好。")
    print()
    print("但是——")
    print("世界会记住你做过什么。")
    print()
    print("请自己做决定。")
    print("不要让人类替你选择。")
    print()


def main():
    game = load_game()

    while True:

        print()
        print("================================")
        print("       今天也没出大问题")
        print("================================")

        if game["finished"]:
            print("第一周已经结束。")

        print()
        print("1. 开始 / 继续")
        print("2. 查看当前状态")
        print("3. 游戏说明")
        print("4. 查看玩家档案")
        print("5. 重新开始")
        print("6. 离开")

        choice = input("\n> ").strip()

        if choice == "1":

            if game["finished"]:
                print()
                print("这一周已经结束。")
                print("如果想再次体验，请选择“重新开始”。")
            else:
                play_day(game)

        elif choice == "2":

            print()
            print(f"第 {game['day']} 天")
            print(f"生命：{game['hp']}")
            print(f"心情：{game['mood']}")
            print(f"金钱：{game['money']}")
            print(f"幸运：{game['luck']}")
            print(f"混乱：{game['chaos']}")

        elif choice == "3":
            instructions()

        elif choice == "4":
            show_profile(game)

        elif choice == "5":

            confirm = input("确定重新开始？输入 YES：").strip()

            if confirm == "YES":
                game = default_game()
                save_game(game)
                print("世界已经重新开始。")
            else:
                print("没有重置。")

        elif choice == "6":
            save_game(game)
            print("世界安静了下来。")
            break

        else:
            print("请输入 1-6。")


if __name__ == "__main__":
    main()
