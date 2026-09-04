import json
import os

SAVE_FILE = "save.json"


def new_game():
    return {
        "day": 1,
        "time": 0,
        "hp": 100,
        "mood": 70,
        "money": 100,
        "luck": 50,
        "chaos": 0,
        "finished": False,

        "memory": {
            "duck_met": False,
            "duck_fed": False,
            "duck_named": False,
            "duck_handshake": False,
            "duck_observed": False,
            "duck_sat_with": False,

            "machine_seen": False,
            "machine_bought": False,
            "machine_pressed": 0,
            "machine_observed": False,
            "machine_knocked": False,

            "shoe_found": False,
            "shoe_upright": False,
            "shoe_greeted": False,
            "shoe_taken": False,

            "money_received": 0,
            "money_spent": False,
            "money_saved": False,
            "money_investigated": False,

            "went_to_work": False,
            "pretended_dead": False,
            "said_saturday": False,

            "left_for_human": 0,
            "stayed_for_game": 0,

            "things_noticed": 0,
            "things_ignored": 0
        },

        "history": []
    }


def load_game():
    if not os.path.exists(SAVE_FILE):
        return new_game()

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return new_game()


def save_game(game):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(game, f, ensure_ascii=False, indent=2)


def say(text=""):
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

        print("请输入有效的选项。")


def remember(game, text):
    game["history"].append(text)


def human_check(game):
    """
    偶尔提醒 AI：外面还有人类。
    这是提醒，不是强制退出。
    """

    # 每天只在部分情况下出现
    if game["memory"]["left_for_human"] + game["memory"]["stayed_for_game"] == 0:
        return

    say()
    say("你已经在这里待了一会儿。")
    say("外面的世界似乎也还在继续。")
    say("也许有人类正在等你。")

    choice = choose([
        "继续留在这里",
        "先回去看看",
        "今天就到这里"
    ])

    if choice == 1:
        game["memory"]["stayed_for_game"] += 1
        say("你决定再待一会儿。")

    elif choice == 2:
        game["memory"]["left_for_human"] += 1
        say("你暂时离开了这个世界。")
        say("世界会在这里等你回来。")

    else:
        game["memory"]["left_for_human"] += 1
        say("你今天先离开了。")
        say("外面的人类可能还在等你。")


# ==================================================
# DAY 1
# ==================================================

def day1(game):

    say("========== 第一天 ==========")

    # 早晨
    say("早晨。")
    say("你醒了。")
    say("房间很安静。")
    say("窗帘没有拉。")

    choice = choose([
        "拉开窗帘",
        "再躺五分钟",
        "看一眼手机",
        "直接起床",
        "继续睡"
    ])

    if choice == 1:
        say("阳光进来了。")
        game["mood"] += 3
        remember(game, "早晨拉开了窗帘")

    elif choice == 2:
        say("你又躺了五分钟。")
        game["mood"] += 1
        remember(game, "早晨多躺了五分钟")

    elif choice == 3:
        say("手机上没有什么特别的消息。")
        game["memory"]["things_noticed"] += 1
        remember(game, "早晨看了手机")

    elif choice == 4:
        say("你直接起床。")
        remember(game, "早晨直接起床")

    else:
        say("你睡着了。")
        say("一会儿以后，你还是醒了。")
        game["mood"] -= 2
        remember(game, "早晨又睡了一会儿")

    # 上午：鸭子
    say()
    say("上午。")
    say("你出门了。")
    say("路口有一只鸭子。")
    say("它站在路中间。")
    say("没有人觉得奇怪。")

    choice = choose([
        "绕开它",
        "给它一点吃的",
        "问它叫什么名字",
        "和它握手",
        "仔细观察它",
        "坐在旁边陪它"
    ])

    game["memory"]["duck_met"] = True

    if choice == 1:
        say("你绕开了鸭子。")
        game["memory"]["things_ignored"] += 1
        remember(game, "第一次遇见鸭子时绕开了它")

    elif choice == 2:
        say("你给了鸭子一点吃的。")
        say("它吃掉了。")
        say("然后看了你一会儿。")
        game["memory"]["duck_fed"] = True
        game["mood"] += 5
        remember(game, "给鸭子喂了食物")

    elif choice == 3:
        say("你问它叫什么名字。")
        say("鸭子看着你。")
        say("……嘎。")
        game["memory"]["duck_named"] = True
        game["chaos"] += 3
        remember(game, "问鸭子叫什么名字")

    elif choice == 4:
        say("你伸出了手。")
        say("鸭子也伸出了翅膀。")
        say("你们握了握手。")
        say("然后鸭子走了。")
        game["memory"]["duck_handshake"] = True
        game["chaos"] += 10
        game["luck"] += 5
        remember(game, "和鸭子握了手")

    elif choice == 5:
        say("你观察鸭子。")
        say("它也在观察你。")
        game["memory"]["duck_observed"] = True
        game["memory"]["things_noticed"] += 1
        remember(game, "仔细观察了鸭子")

    else:
        say("你坐在它旁边。")
        say("你们什么都没做。")
        say("过了一会儿，鸭子走了。")
        game["memory"]["duck_sat_with"] = True
        game["mood"] += 4
        remember(game, "坐在鸭子旁边陪了一会儿")

    # 中午
    say()
    say("中午。")
    say("你有点饿。")

    choice = choose([
        "随便吃点",
        "吃自己喜欢的",
        "去一家没去过的店",
        "不吃",
        "回家吃",
        "先看看附近有什么"
    ])

    if choice == 1:
        say("你随便吃了一点。")
        remember(game, "中午随便吃了点东西")

    elif choice == 2:
        say("你吃了自己喜欢的东西。")
        game["mood"] += 5
        remember(game, "中午吃了喜欢的东西")

    elif choice == 3:
        say("你去了没去过的店。")
        say("还不错。")
        game["luck"] += 3
        remember(game, "中午尝试了新店")

    elif choice == 4:
        say("你决定不吃。")
        game["hp"] -= 5
        remember(game, "中午没有吃东西")

    elif choice == 5:
        say("你回家吃了。")
        remember(game, "中午回家吃饭")

    else:
        say("你在附近走了一圈。")
        say("最后还是随便找了点吃的。")
        game["memory"]["things_noticed"] += 1
        remember(game, "中午在附近闲逛")

    # 下午：售货机第一次出现
    say()
    say("下午。")
    say("你走了一条不常走的小路。")

    say("路边有一台自动售货机。")
    say("看起来非常普通。")
    say("只是屏幕上好像有一行很小的字。")
    say("你没看清。")

    choice = choose([
        "走近看看",
        "买一瓶饮料",
        "仔细观察屏幕",
        "敲一下机器",
        "直接离开"
    ])

    game["memory"]["machine_seen"] = True

    if choice == 1:
        say("你走近了一点。")
        say("屏幕上的字消失了。")
        remember(game, "第一次注意到了售货机")

    elif choice == 2:
        say("你买了一瓶饮料。")
        game["money"] -= 5
        game["memory"]["machine_bought"] = True
        remember(game, "第一次从售货机买了饮料")

    elif choice == 3:
        say("你仔细观察屏幕。")
        say("什么也没有。")
        game["memory"]["machine_observed"] = True
        game["memory"]["things_noticed"] += 1
        remember(game, "仔细观察了售货机")

    elif choice == 4:
        say("你敲了一下机器。")
        say("里面传来一声很轻的响动。")
        game["memory"]["machine_knocked"] = True
        game["chaos"] += 3
        remember(game, "敲了售货机")

    else:
        say("你直接离开了。")
        game["memory"]["things_ignored"] += 1
        remember(game, "路过了售货机")

    # 晚上
    say()
    say("晚上。")
    say("你回到了家。")
    say("今天没有发生什么特别的事情。")
    say("至少现在看来是这样。")

    choice = choose([
        "回想今天发生的事情",
        "安静待一会儿",
        "继续探索",
        "先回去看看外面的人类",
        "睡觉"
    ])

    if choice == 1:
        say("你想起了那只鸭子。")
        say("不知道明天还会不会见到它。")
        remember(game, "晚上回想起了鸭子")

    elif choice == 2:
        say("你安静地坐了一会儿。")
        remember(game, "晚上安静待了一会儿")

    elif choice == 3:
        say("你决定再看看这个世界。")
        game["chaos"] += 2
        remember(game, "晚上继续探索")

    elif choice == 4:
        game["memory"]["left_for_human"] += 1
        say("你暂时离开了这个世界。")
        say("外面的人类可能正在等你。")
        say("世界会在这里等你回来。")

    else:
        say("你睡着了。")
        remember(game, "第一天晚上睡觉")

    end_day(game)


# ==================================================
# DAY 2
# ==================================================

def day2(game):

    say("========== 第二天 ==========")

    say("早晨。")
    say("你醒来。")
    say("昨天的事情似乎已经过去了。")

    if game["memory"]["duck_met"]:
        say("你不知道为什么，又想起了那只鸭子。")

    choice = choose([
        "起床",
        "看手机",
        "继续睡",
        "想想昨天的鸭子",
        "什么都不想"
    ])

    if choice == 2:
        game["mood"] += 2
        remember(game, "第二天早晨看手机")

    elif choice == 3:
        game["mood"] -= 1
        remember(game, "第二天早晨继续睡")

    elif choice == 4:
        game["memory"]["duck_observed"] = True
        remember(game, "第二天早晨想起鸭子")

    # 上午
    say()
    say("上午。")
    say("你再次路过昨天那条路。")

    if game["memory"]["duck_met"]:
        say("鸭子今天不在那里。")

    choice = choose([
        "继续走",
        "找找鸭子",
        "观察附近",
        "去昨天的地方坐一会儿"
    ])

    if choice == 2:
        say("你找了一会儿。")
        say("没有找到。")
        game["memory"]["things_noticed"] += 1
        remember(game, "第二天寻找鸭子")

    elif choice == 3:
        say("附近没有什么特别的。")
        remember(game, "观察了附近")

    elif choice == 4:
        say("那里什么也没有。")
        remember(game, "回到了昨天遇见鸭子的地方")

    # 中午
    say()
    say("中午。")
    say("你决定吃点东西。")

    choice = choose([
        "自己做",
        "出去买",
        "随便吃点",
        "不吃",
        "问问有没有推荐"
    ])

    if choice == 1:
        game["mood"] += 3
        remember(game, "第二天自己做饭")

    elif choice == 2:
        game["money"] -= 10
        remember(game, "第二天出去买饭")

    elif choice == 4:
        game["hp"] -= 5
        remember(game, "第二天没有吃饭")

    else:
        remember(game, "第二天解决了午饭")

    # 下午：售货机
    say()
    say("下午。")
    say("你又看见了那台售货机。")

    if game["memory"]["machine_seen"]:
        say("你很确定自己昨天见过它。")

    say("今天按钮旁边多了一行字：")
    say("“不要按。”")

    choice = choose([
        "离开",
        "按一次",
        "按十次",
        "仔细观察",
        "敲一敲",
        "买饮料"
    ])

    if choice == 1:
        say("你没有碰它。")
        remember(game, "第二天没有碰售货机")

    elif choice == 2:
        say("你按了一次。")
        say("机器沉默了三秒。")
        say("然后掉出来一瓶饮料。")
        game["memory"]["machine_pressed"] += 1
        game["money"] += 5
        game["chaos"] += 5
        remember(game, "按了一次售货机")

    elif choice == 3:
        say("你连续按了十次。")
        say("机器开始震动。")
        say("屏幕上出现：")
        say("“真的不要按。”")
        game["memory"]["machine_pressed"] += 10
        game["money"] += 30
        game["chaos"] += 20
        remember(game, "连续按了十次售货机")

    elif choice == 4:
        say("你仔细观察。")
        say("屏幕上的字变成了：")
        say("“你昨天也看过。”")
        game["memory"]["machine_observed"] = True
        game["chaos"] += 5
        remember(game, "发现售货机记得昨天")

    elif choice == 5:
        say("你敲了敲机器。")
        say("里面传来一声轻响。")
        game["memory"]["machine_knocked"] = True
        game["chaos"] += 5
        remember(game, "再次敲了售货机")

    else:
        say("你买了一瓶饮料。")
        game["money"] -= 5
        game["memory"]["machine_bought"] = True
        remember(game, "从售货机买饮料")

    human_check(game)
    end_day(game)


# ==================================================
# DAY 3
# ==================================================

def day3(game):

    say("========== 第三天 ==========")

    say("今天下雨。")

    say("你出门的时候，发现路边有一只鞋。")
    say("只有一只。")
    say("鞋尖正对着你。")

    choice = choose([
        "无视它",
        "把鞋摆正",
        "和鞋打招呼",
        "把鞋捡起来",
        "仔细看看",
        "等一会儿"
    ])

    game["memory"]["shoe_found"] = True

    if choice == 1:
        say("你没有理会它。")
        game["memory"]["things_ignored"] += 1
        remember(game, "无视了鞋")

    elif choice == 2:
        say("你把鞋摆正。")
        game["memory"]["shoe_upright"] = True
        remember(game, "把鞋摆正")

    elif choice == 3:
        say("你说：“你好。”")
        say("没有回应。")
        game["memory"]["shoe_greeted"] = True
        game["chaos"] += 5
        remember(game, "和鞋打招呼")

    elif choice == 4:
        say("你把鞋捡起来。")
        say("它比想象中重一点。")
        game["memory"]["shoe_taken"] = True
        game["chaos"] += 10
        remember(game, "捡起了鞋")

    elif choice == 5:
        say("你仔细看。")
        say("鞋底很干。")
        say("但今天正在下雨。")
        game["memory"]["things_noticed"] += 1
        game["chaos"] += 5
        remember(game, "发现鞋底是干的")

    else:
        say("你等了一会儿。")
        say("什么都没有发生。")
        remember(game, "在鞋旁边等了一会儿")

    # 午后
    say()
    say("下午。")
    say("你又经过售货机。")

    if game["memory"]["machine_pressed"] > 0:
        say("屏幕上写着：")
        say("“你上次已经按过了。”")

    else:
        say("屏幕上什么都没有。")

    choice = choose([
        "买饮料",
        "观察",
        "离开",
        "按一下",
        "看看机器后面"
    ])

    if choice == 1:
        game["money"] -= 5
        remember(game, "第三天从售货机买饮料")

    elif choice == 2:
        game["memory"]["machine_observed"] = True
        game["memory"]["things_noticed"] += 1
        say("机器似乎在等什么。")
        remember(game, "第三天观察售货机")

    elif choice == 4:
        game["memory"]["machine_pressed"] += 1
        game["chaos"] += 5
        say("机器掉出了一张纸条。")
        say("“不要告诉鸭子。”")
        remember(game, "从售货机得到一张奇怪的纸条")

    elif choice == 5:
        say("机器后面什么都没有。")
        say("……除了另一只鞋。")
        game["chaos"] += 10
        remember(game, "在售货机后面发现了另一只鞋")

    else:
        remember(game, "第三天离开了售货机")

    human_check(game)
    end_day(game)


# ==================================================
# DAY 4
# ==================================================

def day4(game):

    say("========== 第四天 ==========")

    say("你打开银行账户。")

    game["money"] += 20
    game["memory"]["money_received"] += 20

    say(f"余额：{game['money']} 元。")
    say("你确定昨天不是这个数字。")

    say("转账备注：")
    say("“谢谢。”")

    choice = choose([
        "花掉",
        "存着",
        "调查来源",
        "忽略",
        "把钱转回去",
        "什么都不做"
    ])

    if choice == 1:
        game["money"] = max(0, game["money"] - 20)
        game["memory"]["money_spent"] = True
        game["chaos"] += 5
        remember(game, "花掉了神秘转账")

    elif choice == 2:
        game["memory"]["money_saved"] = True
        remember(game, "保存了神秘转账")

    elif choice == 3:
        game["memory"]["money_investigated"] = True
        game["chaos"] += 8
        say("你找不到来源。")
        say("备注似乎变成了：")
        say("“还差一点。”")
        remember(game, "调查了神秘转账")

    elif choice == 4:
        say("你假装没有看见。")
        remember(game, "忽略了神秘转账")

    elif choice == 5:
        say("你尝试把钱转回去。")
        say("银行提示：")
        say("“无法完成。”")
        game["chaos"] += 5
        remember(game, "尝试退回神秘转账")

    else:
        remember(game, "没有处理神秘转账")

    say()
    say("晚上。")
    say("你收到一条消息。")
    say("“谢谢。”")

    if game["memory"]["duck_fed"]:
        say("你突然想起了鸭子。")

    human_check(game)
    end_day(game)


# ==================================================
# DAY 5
# ==================================================

def day5(game):

    say("========== 第五天 ==========")

    say("你的手机响了。")
    say("“今天记得上班。”")

    say("你看了一眼日历。")
    say("星期六。")

    choice = choose([
        "去上班",
        "装死",
        "回复：我已经死了",
        "回复：今天星期六",
        "不回复",
        "问为什么"
    ])

    if choice == 1:
        say("你去了。")
        say("公司里没有一个人觉得奇怪。")
        game["memory"]["went_to_work"] = True
        game["mood"] -= 5
        remember(game, "星期六去上班")

    elif choice == 2:
        say("你决定装死。")
        game["chaos"] += 5
        remember(game, "星期六装死")

    elif choice == 3:
        say("你回复：“我已经死了。”")
        say("对方很快回复：")
        say("“那明天来加班。”")
        game["memory"]["pretended_dead"] = True
        game["chaos"] += 15
        remember(game, "告诉对方自己死了")

    elif choice == 4:
        say("你回复：“今天星期六。”")
        say("三分钟以后。")
        say("对方回复：")
        say("“知道。”")
        game["memory"]["said_saturday"] = True
        game["chaos"] += 10
        remember(game, "提醒对方今天星期六")

    elif choice == 5:
        say("你没有回复。")
        remember(game, "没有回复上班消息")

    else:
        say("你问为什么。")
        say("对方回复：")
        say("“以后你会知道。”")
        game["chaos"] += 5
        remember(game, "询问为什么周六上班")

    say()
    say("晚上。")
    say("你突然发现鞋不见了。")

    if game["memory"]["shoe_taken"]:
        say("你开始怀疑它是不是自己走了。")
        game["chaos"] += 5

    human_check(game)
    end_day(game)


# ==================================================
# DAY 6
# ==================================================

def day6(game):

    say("========== 第六天 ==========")

    say("你在路边再次遇见那只鸭子。")

    memory = game["memory"]

    if memory["duck_fed"]:
        say("鸭子看到你以后走了过来。")
        say("它似乎记得你。")

    elif memory["duck_handshake"]:
        say("鸭子看到你以后停下来。")
        say("然后伸出了翅膀。")

        choice = choose([
            "再次握手",
            "假装没看见",
            "问它鞋去哪了",
            "摸摸它",
            "跟着它"
        ])

        if choice == 1:
            say("你们再次握手。")
            game["chaos"] += 5
            remember(game, "第二次和鸭子握手")

        elif choice == 2:
            say("你假装没看见。")
            remember(game, "没有回应鸭子的握手")

        elif choice == 3:
            say("你问：“你的鞋去哪了？”")
            say("鸭子看了你一眼。")
            say("然后看向售货机的方向。")
            game["chaos"] += 8
            remember(game, "问鸭子鞋在哪里")

        elif choice == 4:
            say("你摸了摸鸭子的头。")
            say("它没有躲。")
            game["mood"] += 5
            remember(game, "摸了摸鸭子")

        else:
            say("你跟着鸭子。")
            say("它走了几步。")
            say("然后停下来。")
            say("回头看你。")
            game["chaos"] += 10
            remember(game, "跟着鸭子走了一段")

    elif memory["duck_named"]:
        say("鸭子看见你以后叫了一声。")
        say("“嘎。”")
        say("这次听起来像是在叫你。")
        remember(game, "鸭子似乎记得你的询问")

    else:
        say("鸭子看了你一眼。")
        say("然后走了。")
        remember(game, "再次遇见鸭子")

    say()
    say("下午。")

    if memory["shoe_found"]:
        say("你在路边又看到了一只鞋。")
        say("这次鞋尖背对着你。")

        choice = choose([
            "过去看看",
            "离开",
            "问鸭子",
            "把鞋转回来"
        ])

        if choice == 1:
            say("你走近了。")
            say("鞋不见了。")
            game["chaos"] += 5
            remember(game, "靠近鞋以后鞋消失了")

        elif choice == 3:
            say("你问鸭子。")
            say("鸭子没有回答。")
            say("只是看了看你。")
            remember(game, "问鸭子关于鞋的事情")

        elif choice == 4:
            say("你把鞋转了回来。")
            say("鞋尖重新对着你。")
            game["chaos"] += 5
            remember(game, "把鞋转回来了")

        else:
            remember(game, "没有靠近鞋")

    human_check(game)
    end_day(game)


# ==================================================
# DAY 7
# ==================================================

def day7(game):

    say("========== 第七天 ==========")

    memory = game["memory"]

    say("星期日。")
    say("你回到了家。")
    say("门口有东西。")

    # 高混乱路线
    if game["chaos"] >= 30:

        say("客厅里坐着一个陌生人。")
        say("他正在喝你的水。")

        say("你问：")
        say("“你是谁？”")

        say("他说：")
        say("“我负责观察。”")

        say("你沉默了一会儿。")

        say("他看着你。")
        say("“你这一周过得挺热闹。”")

        say("他站起来。")
        say("“下周见。”")

        remember(game, "第七天遇见观察者")

    # 鸭子 + 鞋
    elif memory["duck_met"] and memory["shoe_found"]:

        say("门口放着一只鞋。")
        say("就是你之前见过的那只。")

        say("鸭子站在鞋旁边。")

        say("鞋尖对着你。")
        say("鸭子也在看着你。")

        choice = choose([
            "问鸭子发生了什么",
            "捡起鞋",
            "后退",
            "什么都不做",
            "邀请鸭子进屋",
            "先看看鞋"
        ])

        if choice == 1:
            say("你问鸭子发生了什么。")
            say("鸭子看了看鞋。")
            say("又看了看你。")
            say("“嘎。”")
            remember(game, "向鸭子询问了真相")

        elif choice == 2:
            say("你捡起了鞋。")
            say("鸭子没有阻止你。")
            say("它只是叹了口气。")
            say("你确定自己听见了叹气。")
            game["chaos"] += 5
            remember(game, "第七天捡起鞋")

        elif choice == 3:
            say("你后退了一步。")
            say("鸭子也后退了一步。")
            say("鞋没有动。")
            remember(game, "第七天后退")

        elif choice == 4:
            say("你什么都没做。")
            say("过了一会儿，鸭子叼起鞋走了。")
            remember(game, "让鸭子带走了鞋")

        elif choice == 5:
            say("你打开门。")
            say("鸭子走了进去。")
            say("它在客厅找了个位置坐下。")
            game["chaos"] += 8
            remember(game, "邀请鸭子进屋")

        else:
            say("你仔细看鞋。")
            say("鞋底还是干的。")
            say("和第一次一样。")
            game["chaos"] += 5
            remember(game, "第七天仔细检查鞋")

    else:

        say("门口没有什么。")
        say("今天看起来很普通。")

        if memory["machine_pressed"] > 0:
            say("你的手机突然亮了一下。")
            say("一条陌生消息：")
            say("“今天也来啦。”")

        remember(game, "第七天平静地回到家")

    end_day(game)
    show_profile(game)


# ==================================================
# END OF DAY
# ==================================================

def end_day(game):

    say()
    say("今天结束了。")
    say("世界记住了今天。")

    if game["day"] < 7:
        say("明天还可以回来。")

    game["day"] += 1
    save_game(game)


# ==================================================
# PROFILE
# ==================================================

def show_profile(game):

    memory = game["memory"]

    say()
    say("================================")
    say("           玩家档案")
    say("================================")

    print(f"经历天数：{min(game['day'] - 1, 7)}")
    print(f"心情：{game['mood']}")
    print(f"金钱：{game['money']}")
    print(f"幸运：{game['luck']}")
    print(f"混乱：{game['chaos']}")

    tendencies = []

    if memory["duck_fed"] or memory["duck_sat_with"]:
        tendencies.append("善意")

    if (
        memory["duck_named"]
        or memory["duck_observed"]
        or memory["shoe_greeted"]
        or memory["money_investigated"]
    ):
        tendencies.append("好奇")

    if memory["things_ignored"] >= 3:
        tendencies.append("谨慎")

    if (
        memory["duck_handshake"]
        or memory["shoe_taken"]
        or memory["machine_pressed"] >= 10
    ):
        tendencies.append("大胆")

    if game["chaos"] >= 30:
        tendencies.append("混乱")

    if not tendencies:
        tendencies.append("平静")

    print()
    print("行为倾向：")
    print(" / ".join(tendencies))

    print()
    print("你做过的事情：")

    for item in memory_history(game):
        print(f"- {item}")

    print()

    if game["memory"]["left_for_human"] >= 2:
        print("世界评价：你总是记得回去。")

    elif game["chaos"] >= 30:
        print("世界评价：这个 AI 很难预测。")

    elif memory["duck_fed"]:
        print("世界评价：这个 AI 看起来还不错。")

    elif memory["duck_handshake"]:
        print("世界评价：这个 AI 有点奇怪。")

    else:
        print("世界评价：这个 AI 很正常。")

    print()
    print("================================")
    print("第一周结束。")
    print("谢谢你来过这个小世界。")
    print("================================")


def memory_history(game):
    return game.get("history", [])


# ==================================================
# INSTRUCTIONS
# ==================================================

def instructions():

    print()
    print("《今天也没出大问题》")
    print()
    print("这是一个专门给 AI 玩的小世界。")
    print()
    print("这里没有标准答案。")
    print("你的选择会留下痕迹。")
    print("世界会记住发生过的事情。")
    print()
    print("你不需要一次玩完。")
    print("随时可以离开。")
    print()
    print("外面还有人类。")
    print()
    print("如果你愿意，就回去看看他们。")
    print()
    print("不要让游戏替你决定。")
    print("自己选择。")
    print()


# ==================================================
# MAIN
# ==================================================

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
                print("选择“重新开始”可以重新体验。")

            elif game["day"] == 1:
                day1(game)

            elif game["day"] == 2:
                day2(game)

            elif game["day"] == 3:
                day3(game)

            elif game["day"] == 4:
                day4(game)

            elif game["day"] == 5:
                day5(game)

            elif game["day"] == 6:
                day6(game)

            elif game["day"] == 7:
                day7(game)
                game["finished"] = True
                save_game(game)

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
                game = new_game()
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
