‎from telegram import Update
‎from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
‎
‎BOT_TOKEN = "8961826562:AAHc4Rlihi-u9mhwZXxcziRgK9vYySVF5Pk
‎ADMIN_ID = 8224572892
‎
‎async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
‎    await update.message.reply_text(
‎        "👋 Welcome!\n\nApni support request ek message me bhej dijiye."
‎    )
‎
‎async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
‎    user = update.effective_user
‎
‎    text = f"""
‎📩 New Support Request
‎
‎👤 Name: {user.full_name}
‎🆔 ID: {user.id}
‎📛 Username: @{user.username}
‎
‎📝 Message:
‎{update.message.text}
‎"""
‎
‎    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
‎    await update.message.reply_text("✅ Aapki request admin ko bhej di gayi hai.")
‎
‎app = Application.builder().token(BOT_TOKEN).build()
‎
‎app.add_handler(CommandHandler("start", start))
‎app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
‎
‎app.run_polling()
