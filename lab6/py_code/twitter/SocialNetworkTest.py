import pytest
from datetime import datetime
from SocialNetwork import SocialNetwork
from Tweet import Tweet

# Test if assertions are enabled
def test_assertions_enabled():
    with pytest.raises(AssertionError):
        assert False, "Assertions should be enabled."

# Test case for an empty follows graph (no tweets)
def test_guess_follows_graph_empty():
    tweets = []
    follows_graph = SocialNetwork.guess_follows_graph(tweets)
    assert len(follows_graph) == 0, "Expected an empty graph when there are no tweets."

# Test case for extracting mentions (no mentions)
def test_extract_mentions_no_mentions():
    text = "This is a tweet with no mentions."
    mentions = SocialNetwork.extract_mentions(text)
    assert len(mentions) == 0, "Expected no mentions."

# Test case for extracting mentions (single mention)
def test_extract_mentions_single_mention():
    text = "This is a tweet mentioning @userA."
    mentions = SocialNetwork.extract_mentions(text)
    assert mentions == {'usera'}, "Expected to extract userA."

# Test case for extracting multiple mentions
def test_extract_mentions_multiple_mentions():
    text = "@userA mentioned @userB and @userC."
    mentions = SocialNetwork.extract_mentions(text)
    assert mentions == {'usera', 'userb', 'userc'}, "Expected to extract multiple mentions."

# Test case for extracting mentions (case insensitivity)
def test_extract_mentions_case_insensitivity():
    text = "@UserA @usera"
    mentions = SocialNetwork.extract_mentions(text)
    assert mentions == {'usera'}, "Expected mentions to be case-insensitive."

# Test case where one tweet mentions a single user
def test_guess_follows_graph_single_mention():
    tweet = Tweet(id=1, author="userA", text="mentioning @userB", timestamp=datetime.now())
    tweets = [tweet]
    follows_graph = SocialNetwork.guess_follows_graph(tweets)
    assert follows_graph == {'usera': {'userb'}}, "Expected userA to follow userB."

# Test case where one tweet mentions multiple users
def test_guess_follows_graph_multiple_mentions():
    tweet = Tweet(id=2, author="userA", text="mentioning @userB and @userC", timestamp=datetime.now())
    tweets = [tweet]
    follows_graph = SocialNetwork.guess_follows_graph(tweets)
    assert follows_graph == {'usera': {'userb', 'userc'}}, "Expected userA to follow both userB and userC."

# Test case with multiple tweets from different users
def test_guess_follows_graph_multiple_tweets():
    tweet1 = Tweet(id=1, author="userA", text="mentioning @userB", timestamp=datetime.now())
    tweet2 = Tweet(id=2, author="userB", text="mentioning @userA and @userC", timestamp=datetime.now())
    tweets = [tweet1, tweet2]
    follows_graph = SocialNetwork.guess_follows_graph(tweets)
    expected_graph = {
        'usera': {'userb'},
        'userb': {'usera', 'userc'}
    }
    assert follows_graph == expected_graph, "Expected a follows graph with multiple users."

# Test case with self-mention (user mentioning themselves)
def test_guess_follows_graph_self_mention():
    tweet = Tweet(id=3, author="userA", text="mentioning @userA", timestamp=datetime.now())
    tweets = [tweet]
    follows_graph = SocialNetwork.guess_follows_graph(tweets)
    assert follows_graph == {'usera': {'usera'}}, "Expected userA to follow themselves."

# Test influencers sorted by follower count
def test_influencers_sorted():
    follows_graph = {
        'usera': {'userb', 'userc'},
        'userb': {'userc'},
        'userc': set()
    }
    influencers_list = SocialNetwork.influencers(follows_graph)
    assert influencers_list == ['userc', 'userb'], "Expected userC to be the top influencer, followed by userB."

# Test influencers when no one is followed
def test_influencers_no_followers():
    follows_graph = {
        'usera': set(),
        'userb': set()
    }
    influencers_list = SocialNetwork.influencers(follows_graph)
    assert influencers_list == [], "Expected no influencers when no one is followed."

# Test case where a tweet has no mentions
def test_guess_follows_graph_no_mentions():
    tweet = Tweet(id=4, author="userA", text="This tweet has no mentions.", timestamp=datetime.now())
    tweets = [tweet]
    follows_graph = SocialNetwork.guess_follows_graph(tweets)
    assert follows_graph == {'usera': set()}, "Expected userA to follow no one."

