from datetime import datetime
class Publication:
    def __init__(self, text):
        self.text = text
    def form_text_to_publish(self):
        return self.text
    def publish(self, file_name):
        with open(file_name, 'a') as file:
            file.write(self.form_text_to_publish())
class News(Publication):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
    def form_text_to_publish(self):
        text_to_publish = "--------------------\n" + self.text + "\n" + self.city + '\n' + str(datetime.now()) + '\n' + '--------------------'+ '\n'
        return text_to_publish
a = News('Emergency rescue operations completed at the site of the airstrike in Kharkiv','Kharkiv')
a.publish('News_feed.txt')
