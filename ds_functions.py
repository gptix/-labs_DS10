def build_model_tweets_per_user_id(user_id):
    """Given a user ID, get a representative set of tweets from twitter,
including the time, the number of enggements, and maybe some other parameters.
Build and fit a model that can be used to predict a best time to tweet, based
on user_id."""
    
    # make twitter connection
    conn = twitter_magic(our_id)
    tweets = conn.give_tweets(userID, 60days)
    tweets_df = pd.DataFrame(tweets)
    tweets_df = clean_data(tweets_df)
    X = tweets_df['user_id']
    y = tweets_df['clicks']
    
    our_model = someClass()
    our_model.fit(X,y)
    # pickle model?  Name it based on user_id?
    return our_model


def best_time_by_user_id(user_id):
"""Return the best time for a tweet based on user_id.  Use a preexisting
model if one exists. make a new one if it does not yet exist."""
    if (a_model_exists_yet(user_id)):
        mod = un_pickle_model(user_id)
    else:
        mod = build_model_tweets_per_user_id(user_id)

    return function_that_retrieves_best_time(user_id)


def function_that_retrieves_best_time(uid):
    """Actually use the fitted model to get a best time to tweet."""
    pass
    
