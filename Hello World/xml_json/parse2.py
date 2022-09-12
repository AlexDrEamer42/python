import xml.etree.ElementTree as ET

def top_10(input):
    # Магия чтения из XML
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("/home/alex/Python/python/Hello World/xml_json/files/newsafr.xml",parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")
    # Вытаскиваем тексты новостей, пилим на слова и составляем список из всех, что длиннее 6 символов
    words = []
    for news in xml_items:
        news_words = news.find("description").text.split(' ')
        for word in news_words:
            if len(word) > 6:
                words.append(word)
    # Формируем множество уникальных слов
    unique_words = set(words)
    # Создаём словарь с количеством вхождений каждого уникального слова
    number = {}
    for word in unique_words:
        number[word] = words.count(word)
    # Сортируем по значениям от большего к меньшему
    sorted_number = dict(sorted(number.items(), reverse = True, key=lambda item: item[1]))
    # Делаем выборку из 10 первых значений
    i = 0
    top_words = {}
    for word in sorted_number:
        i +=1
        top_words[word] = sorted_number[word]
        if i == 10:
            break
    return top_words

input_file = "/home/alex/Python/python/Hello World/xml_json/files/newsafr.xml"
print(top_10(input_file))