#!/usr/bin/python3
import twitter
import time
import cache
import discord


def main():
    cache_manager = cache.CacheManager()

    discord_manager = discord.DiscordManager()

    twit = twitter.TwitterStreamListener(cache_manager, discord_manager)

    print('Bot ready')
    while twit.is_running():
        time.sleep(1)


if __name__ == '__main__':
    main()
