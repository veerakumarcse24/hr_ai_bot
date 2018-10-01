# -*- coding: utf-8 -*-

from textblob import TextBlob

def languageTranslate(inputData):
    source_language = TextBlob(u'வணக்கம்')
    return (source_language.translate(to='en'))
