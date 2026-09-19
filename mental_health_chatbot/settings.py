BOT_NAME = "mental_health_chatbot"

SPIDER_MODULES = ["mental_health_chatbot.spiders"]
NEWSPIDER_MODULE = "mental_health_chatbot.spiders"

ROBOTSTXT_OBEY = True

TWISTED_REACTOR = (
    "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
)

FEED_EXPORT_ENCODING = "utf-8"