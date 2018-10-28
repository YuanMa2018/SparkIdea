# coding:utf-8
from bs4 import BeautifulSoup
import re


def get_content(realLink, HTMLString):
    title = ''
    content = ''
    if HTMLString is not None and realLink is not None:

        try:
            soup = BeautifulSoup(HTMLString, 'html.parser', from_encoding='utf-8')


            if "https://twitter.com" in realLink:
                print('--------END--------useless link')
                return

            if "http://www.bbc." in realLink:
                title_node = soup.find('h1', class_=re.compile(r"story-body__h1"))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"story-body__inner"))
                p_node = link_node.find_all('p')
                for p in p_node:
                    content += p.get_text()
                return title, content

            elif "https://www.theguardian.com/" in realLink:
                title_node = soup.find('h1', class_=re.compile(r"content__headline"))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"content__article-body"))
                p_node = link_node.find_all('p')
                for p in p_node:
                    if p.get('class') is None:
                        content += p.get_text()
                return title, content

            elif "reuters.com" in realLink:
                title_node = soup.find('h1', class_=re.compile(r"headline"))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"body_1gnLA"))
                p_node = link_node.find_all('p')
                for p in p_node:
                    content += p.get_text()
                return title, content

            elif "www.express" in realLink:

                title_node = soup.find('h1', itemprop=re.compile(r"headline"))
                title = title_node.get_text()
                Firstsentence = title_node.parent.find('h3')
                if Firstsentence is not None:
                    content += Firstsentence.get_text()
                link_nodeList = soup.find_all('section', class_=re.compile(r"text-description"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.dailymail" in realLink:
                title_node = soup.find('h1') #, id="ext-gen6"
                title = title_node.get_text()
                link_nodeList = soup.find_all('div', itemprop=re.compile(r"articleBody"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.washingtonpost" in realLink:

                title_node = soup.find('h1', itemprop=re.compile(r"headline"))
                title = title_node.get_text()
                link_nodeList = soup.find_all('article', itemprop=re.compile(r"articleBody"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.buzzfeed" in realLink:

                title_node = soup.find('h1', class_=re.compile(r"buzz-title"))
                title = title_node.get_text()
                content += soup.find('p', class_=re.compile(r"buzz-dek xs-mb1 md-mb2")).get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"subbuzz-text"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.dailywire" in realLink:

                title_node = soup.find('h1', class_=re.compile(r"page-title title"))
                title = title_node.get_text()
                content += soup.find('h2', class_=re.compile(r"subtitle")).get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"field-body"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content


            elif "www.nytimes" in realLink:

                title_node = soup.find('h1', class_=re.compile(r"headline"))
                title = title_node.get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"story-body story-body"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()

                return title, content

            elif "www.telegraph" in realLink:

                title_node = soup.find('h1', itemprop=re.compile(r"headline name"))
                title = title_node.get_text()
                link_nodeList = soup.find_all('article', itemprop=re.compile(r"articleBody"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "news.sky" in realLink:

                title_node = soup.find('h1', class_=re.compile(r"sdc-news-article-header__headline "))
                title = title_node.get_text()
                content += title_node.parent.find('p', class_=re.compile(r"sdc-news-article-header__standfirst")).get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"sdc-news-story-article"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.mirror" in realLink:

                title_node = soup.find('h1', itemprop=re.compile(r"headline name"))
                title = title_node.get_text()
                content += title_node.parent.find('p', itemprop=re.compile(r"description")).get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"article-body"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.breitbart" in realLink:

                title_node = soup.find('header', class_=re.compile(r"articleheader")).find('h1')
                title = title_node.get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"entry-content"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.zerohedge" in realLink:

                title_node = soup.find('h1', class_=re.compile(r"page-title"))
                title = title_node.get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"field field--name-body field--type-text-with-summary"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.rt" in realLink:

                title_node = soup.find('h1', class_=re.compile(r"article__heading"))
                title = title_node.get_text()
                content += soup.find('div', class_=re.compile(r"article__summary summary ")).get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"article__text text "))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content

            elif "www.politico" in realLink:

                title_node = soup.find('div', class_=re.compile(r'story-intro format-')).find('header').find('h1')
                title = title_node.get_text()
                link_nodeList = soup.find_all('div', class_=re.compile(r"story-text has-sidebar"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                        return title, content


            elif "www.thepoke" in realLink:

                title_node = soup.find('div', class_=re.compile(r'post')).find('h1')
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"entry"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content


            elif "www.channelnewsasia" in realLink:

                title_node = soup.find('h1', class_=re.compile(r'article__title'))
                title = title_node.get_text()
                temp = soup.find('div', class_=re.compile(r"article__abstract"))
                if temp is not None:
                    content += temp.find('p').get_text()
                link_node = soup.find('div', class_=re.compile(r"c-rte--article"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content


            elif "www.thesun" in realLink:

                title_node = soup.find('h1', class_=re.compile(r'article__headline'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"article__content"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "thenational.scot" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'headline'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"article-body")).find('div')
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "www.20minutes." in realLink:
                title_node = soup.find('h1', class_=re.compile(r'nodeheader-title'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"lt-endor-body content"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "inews.co" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'entry-title article__heading'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"entry-content article__body"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content


            elif "www.dailystar.co" in realLink:
                title_node = soup.find('h1', itemprop=re.compile(r'headline'))
                title = title_node.get_text()
                link_nodeList = soup.find_all('section', class_=re.compile(r"text-description"))
                for link_node in link_nodeList:
                    p_node = link_node.find_all('p')
                    if p_node != []:
                        for p in p_node:
                            content += p.get_text()
                return title, content


            elif "www.eveningtimes.co" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'headline semi-loud'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"article-body"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content


            elif "100percentfedup.com" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'entry-title'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"entry-content"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "www.abc.net" in realLink:
                title_node = soup.find('div', class_=re.compile(r'article section')).find('h1')
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"article section"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content


            elif "www.foxnews" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'headline head1'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"article-body"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "www.thetimes" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'Article-headline Headline Headline--article'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"Article-content"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "www.plymouthherald" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'section-theme-background-indicator publication'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"article-body"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "newsthump.com" in realLink:
                title_node = soup.find('h1', class_=re.compile(r'entry-title'))
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"format_text entry-content"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content

            elif "newstarget" in realLink:
                title_node = soup.find('div', class_=re.compile(r'PostTitle')).find('h1')
                title = title_node.get_text()
                link_node = soup.find('div', class_=re.compile(r"PostArticle"))
                p_node = link_node.find_all('p')
                if p_node != []:
                    for p in p_node:
                        content += p.get_text()
                    return title, content
            # elif "www.news18" in realLink:
            #     importantNode = soup.find('div', class_=re.compile(r'section-blog-left-aricle article_page clearfix'))
            #     title = importantNode.find('h1').get_text()
            #     if importantNode.find('h2', class_=re.compile(r"story-intro")) is not None:
            #         content += importantNode.find('h2', class_=re.compile(r"story-intro")).get_text()
            #     link_node = soup.find('div', class_=re.compile(r"hideCont clearfix paragraph"))
            #     content += link_node.get_text()
            #     # p_node = link_node.find_all('br')
            #     # if p_node != []:
            #     #     for p in p_node:
            #     #         content += p.get_text()
            #     return title, content
            else:
                print('--------END--------unknow link')
                return

        except:
            print 'Exception in GetContentFromLinks'
            pass

