import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Vítejte! 👋\nToto je ukázkový chatbot květinářství 🌸\n\n"
        "Napište jednu z možností:\n"
        "/cenik – Zobrazím přehled základních cen\n"
        "/objednatKvetiny – Ukážu, jak by šla vytvořit objednávka\n"
        "/doruceniKvetin – Řeknu, jak by fungovalo doručení\n"
        "/casteDotazy – Odpovím na běžné otázky"
    )

@bot.message_handler(commands=['cenik'])
def handle_cenik(message):
    bot.send_message(
        message.chat.id,
        "🌷 ZÁKLADNÍ CENÍK (ukázka):\n\n"
        "• Malá kytice – od 249 Kč\n"
        "• Střední kytice – od 399 Kč\n"
        "• Luxusní kytice – od 749 Kč\n"
        "• Doručení po Praze – 99–149 Kč"
    )

@bot.message_handler(commands=['objednatKvetiny'])
def handle_objednat(message):
    bot.send_message(
        message.chat.id,
        "📝 Objednávka (ukázka):\n\n"
        "1. Vyberte typ kytice:\n"
        "/mala – Malá\n/stredni – Střední\n/luxusni – Luxusní\n\n"
        "(Tato verze je pouze ukázková.)"
    )

@bot.message_handler(commands=['doruceniKvetin'])
def handle_doruceni(message):
    bot.send_message(
        message.chat.id,
        "🚚 Doručujeme květiny po celé Praze.\n\n"
        "• Doručení ve stejný den: do 17:00 objednávka\n"
        "• Cena doručení: od 99 Kč\n"
        "• Možnost doručení anonymně 🌹"
    )

@bot.message_handler(commands=['casteDotazy'])
def handle_dotazy(message):
    bot.send_message(
        message.chat.id,
        "❓ Nejčastější dotazy:\n\n"
        "• Kdy máte otevřeno?\nPo–Pá 9:00–18:00, So 10:00–13:00\n\n"
        "• Můžu si objednat i přes telefon?\nAno, samozřejmě.\n\n"
        "• Děláte i svatební kytice?\nAno, po domluvě."
    )

@bot.message_handler(commands=['mala', 'stredni', 'luxusni'])
def handle_typ(message):
    bot.send_message(
        message.chat.id,
        "Super! V reálné verzi bych teď požádal o adresu a datum doručení 🌸"
    )

bot.polling()
