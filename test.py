import colorama
colorama.init()

version = getattr(colorama, '__version__', 'unknown')
if version == '0.4.4':
    print(colorama.Fore.GREEN + f" Установлена версия: {version}")
else:
    print (colorama.Fore.RED + f" Установлена версия: {version}")

#colorama.init()
#print(colorama.Fore.GREEN + " Зеленый текст работает!")