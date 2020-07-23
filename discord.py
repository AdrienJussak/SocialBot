import os
from discord_webhook import DiscordWebhook


class DiscordManager:

    def send_message(self, message: str):
        webhook = DiscordWebhook(url=os.environ['DISCORD_WEBHOOK_URL'], content=message)
        webhook.execute()
