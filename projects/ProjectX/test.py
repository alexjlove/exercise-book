scores_list = []
for city in city['city']:
    url = 'https://twitter.com/search?q=%23' + hashtag + '%20near%3A%22' + city + '%22%20within%3A' + rang + 'mi&src=typd'
    twitter = requests.get(url)
    soup = BeautifulSoup(twitter.text, 'lxml')
    tweet_text = soup.find_all('p', 'js-tweet-text')
    tweets = []
    for i in range(0, len(tweet_text)):
        tweets.append(tweet_text[i].get_text().encode('ascii', 'ignore'))
    tweet_token = []
    for i in range(len(tweets)):
        tweet_token.append(nltk.word_tokenize(tweets[i]))
    bad_elements = ['#', ':', 'pic.twitter', '@', '&', ';', '<', '>', '.', '/' ,',']
    hacked_up = []
    hacked_up_list = []
    for i in range(len(tweet_token)):
        for j in range(len(tweet_token[i])):
            bad_count = 0
            for e in bad_elements:
                if e in tweet_token[i][j]:
                    bad_count = 1
            if bad_count == 0:
                hacked_up.append(tweet_token[i][j])
        hacked_up_list.append(hacked_up)
        hacked_up = []
    scores = []
    for i in range(len(hacked_up_list)):
        scores.append(counts(hacked_up_list[i]))
    total_score = sum(scores)
    scores_list.append(total_score)
city['sentiment'] = scores_list