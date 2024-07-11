import time
import threading
import keyboard
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import ctypes

# Флаг блокировки клавиатуры
is_locked = False

# Таймер для отслеживания активности клавиатуры
activity_timer = None

# Период бездействия в секундах (12 минут)
idle_period = 12 * 60

# Список заблокированных клавиш
blocked_keys = list(range(150)) + list(keyboard.all_modifiers)

def show_blocked_message():
    ctypes.windll.user32.MessageBoxW(0, "Клавиатура заблокирована, можете разблокировать в tray", "Ошибка", 0x10)

def block_keyboard():
    global is_locked
    is_locked = True
    for key in blocked_keys:
        keyboard.block_key(key)
    keyboard.hook(block_event)
    update_menu()

def unblock_keyboard(icon=None, item=None):
    global is_locked
    is_locked = False
    for key in blocked_keys:
        keyboard.unblock_key(key)
    keyboard.unhook(block_event)
    reset_activity_timer()
    update_menu()

def lock_keyboard_manually(icon, item):
    block_keyboard()

def block_event(event):
    if is_locked:
        show_blocked_message()
        return False
    return True

def on_key_event(event):
    reset_activity_timer()

def reset_activity_timer():
    global activity_timer
    if activity_timer:
        activity_timer.cancel()
    if not is_locked:
        activity_timer = threading.Timer(idle_period, block_keyboard)
        activity_timer.start()

def create_image():
    # Создание иконки для трея
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), 'white')
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10),
        fill='black')
    return image

def exit_app(icon, item):
    icon.stop()
    if activity_timer:
        activity_timer.cancel()
    keyboard.unhook_all()

def setup_tray():
    global icon
    icon = pystray.Icon("keyboard_blocker")
    update_menu()
    icon.icon = create_image()
    icon.run()

def update_menu():
    global icon
    icon.menu = pystray.Menu(
        item(
            'Unlock Keyboard',
            unblock_keyboard,
            enabled=lambda item: is_locked
        ),
        item(
            'Lock Keyboard',
            lock_keyboard_manually,
            checked=lambda item: is_locked
        ),
        item(
            'Exit',
            exit_app
        )
    )
    icon.update_menu()

if __name__ == "__main__":
    # Начало отслеживания активности клавиатуры
    keyboard.hook(on_key_event)
    reset_activity_timer()
    
    # Запуск иконки в трее в отдельном потоке
    tray_thread = threading.Thread(target=setup_tray)
    tray_thread.start()
