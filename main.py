from action import *

action = Action()
print('open 雷電多開器')
action.open_muilty_manager()
action.loop_window_show(1, '雷電多開器')     # 確認窗口開啟

action.emulator_start_up()
# action.standby(8)
# action.start_mapleM()
# action.standby(40)
# action.close_events()
# action.click_logo()
# action.choose_world()
# action.start_game()
# action.auto_fight_result()
# action.auto_fight()
# action.auto_fight_use()
# action.auto_fight_start()