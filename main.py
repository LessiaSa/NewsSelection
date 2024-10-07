import collections
import json
import xml.etree.ElementTree as ET

with open("newsafr.json", encoding='utf-8') as f:
    json_data = json.load(f)

words = []

for value in json_data["rss"]["channel"]["items"]:
    description = value["description"]
    news = description.lower().split()
    for word in news:
        if len(word) > 6:
            words.append(word)

word_count = {}
for item in words:
  if item not in word_count:
    word_count[item] = 1
  else:
    word_count[item] += 1

my_words = []

for keys, values in word_count.items():
    my_words.append((values,keys))
    my_words.sort(reverse = True)

for key, val in my_words[:10]:
  print (key, val)



from collections import Counter

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
news_xml = root.findall("channel/items")
news = collections.Counter(news_xml).most_common(3)
print(news)


# def read_xml(file, len_word=6, top_words=10):
#    tree = ET.parse(file)
#    root = tree.getroot()
#    xml_items = root.findall('channel/item')
#    description_words = []
#    descriptions = [item.find('description').text.split() for item in xml_items]
#    for description in descriptions:
#        description = [word for word in description if len(word) > len_word]
#        description_words.extend(description)
#    counter_words = collections.Counter(description_words)
#    pprint(counter_words.most_common(top_words))
#
#
# if __name__ == '__main__':
#    print('------')
#    read_xml('newsafr.xml')
