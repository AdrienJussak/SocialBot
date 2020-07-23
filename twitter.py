import tweepy
import os
import cache
import discord


class TwitterException(Exception):
    pass


class TwitterStreamListener(tweepy.StreamListener):

    def __init__(self, cache_manager: cache.CacheManager, discord_manager: discord.DiscordManager):
        super().__init__()

        self.discord = discord_manager

        auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET'])
        auth.set_access_token(os.environ['TWITTER_USER_KEY'], os.environ['TWITTER_USER_SECRET'])

        api = tweepy.API(auth)

        twitter_cache = cache_manager.get_data('twitter')

        twitter_accounts = os.environ['TWITTER_ACCOUNTS'].split(',')

        follow = []

        for screen_name in twitter_accounts:
            if screen_name in twitter_cache:
                follow.append(twitter_cache[screen_name])
            else:
                user_id = str(api.get_user(screen_name).id)
                follow.append(user_id)
                twitter_cache[screen_name] = user_id

        cache_manager.set_data('twitter', twitter_cache)

        self.myStream = tweepy.Stream(auth=auth, listener=self)
        self.myStream.filter(follow=follow, is_async=True)

    def stop_daemon(self):
        self.myStream.disconnect()

    def on_status(self, status):
        if not hasattr(status, 'retweeted_status'):
            tweet_link = "https://twitter.com/" + status.user.screen_name + "/status/" + status.id_str
            self.discord.send_message(status.user.name + ' a tweeté : \n' + tweet_link)

    def on_error(self, status_code):
        if status_code == 420:
            raise TwitterException()
