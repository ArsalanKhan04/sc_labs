from typing import List, Set, Dict
from Tweet import Tweet
from collections import defaultdict, Counter


class SocialNetwork:

    @staticmethod
    def guess_follows_graph(tweets: List[Tweet]) -> Dict[str, Set[str]]:
        """
        Guess who might follow whom, based on @-mentions in tweets.
        
        Args:
            tweets: a list of Tweet objects providing the evidence.
            
        Returns:
            A dictionary where the keys are Twitter usernames (authors),
            and the values are sets of usernames (those who are @-mentioned).
        """
        follows_graph = defaultdict(set)

        for tweet in tweets:
            author = tweet.author.lower()  # case-insensitive usernames
            mentioned_users = SocialNetwork.extract_mentions(tweet.text)
            follows_graph[author].update(mentioned_users)
        
        return follows_graph

    @staticmethod
    def extract_mentions(text: str) -> Set[str]:
        """
        Extracts mentioned usernames from a tweet text.
        
        Args:
            text: the text of a tweet.
            
        Returns:
            A set of mentioned usernames (case-insensitive).
        """
        import re
        mentions = set(re.findall(r'(?<!\w)@([A-Za-z0-9_-]+)', text))  # Use regex to extract mentions
        return {mention.lower() for mention in mentions}  # Normalize to lowercase

    @staticmethod
    def influencers(follows_graph: Dict[str, Set[str]]) -> List[str]:
        """
        Find the most influential people, based on follower count.
        
        Args:
            follows_graph: a social network dictionary.
            
        Returns:
            A list of distinct usernames sorted by the number of followers, in descending order.
        """
        follower_count = Counter()

        for followed_users in follows_graph.values():
            for user in followed_users:
                follower_count[user] += 1

        # Sort by follower count in descending order
        return [user for user, count in follower_count.most_common()]

