from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функція-обробник команди /start
def start(update, context):
    update.message.reply_text(
        "Привіт! Я бот-калькулятор. \n"
        "Введи вираз у форматі 'число операція число' (наприклад, 5 + 3 або 10 / 2). \n"
        "Підтримую +, -, *, /."
    )

# Функція-обробник для обчислень
def calculate(update, context):
    user_text = update.message.text
    try:
        # Розбиваємо текст на частини по пробілах
        parts = user_text.split()
        if len(parts) != 3:
            update.message.reply_text("Помилка формату! Введи з пробілами, наприклад: 5 + 3")
            return
        
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        
        # Логіка калькулятора
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                update.message.reply_text("Помилка: Ділення на нуль неможливе!")
                return
            result = num1 / num2
        else:
            update.message.reply_text("Невідома операція. Підтримуються лише +, -, *, /")
            return
        
        # Відправляємо результат
        update.message.reply_text(f"Результат: {result}")
        
    except ValueError:
        update.message.reply_text("Помилка: Переконайся, що ти ввів правильні числа.")
    except Exception as e:
        update.message.reply_text("Щось пішло не так. Спробуй ще раз.")

def main():
    # Встав сюди свій токен, отриманий від @BotFather
    TOKEN = "ТВІЙ_ТОКЕН_ТУТ"
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Реєструємо обробники
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate))

    # Запускаємо бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()