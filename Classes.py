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
        text_to_publish = 'News--------------------'+ '\n' + self.text + "\n" + self.city + '\n' + str(datetime.now().date()) + '\n'
        return text_to_publish
class PrivateAd(Publication):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = expiration_date
    def form_text_to_publish(self):
        target_date = datetime.strptime(self.expiration_date, "%Y-%m-%d").date()
        date_difference = target_date - datetime.now().date()
        text_to_publish = 'Private advertisement--------------------'+ '\n' +self.text + "\n" + '\n' + str(date_difference.days) + ' days left' + '\n'
        return text_to_publish
class RestaurantReview(Publication):
    def __init__(self, text, rating):
        super().__init__(text)
        self.rating=rating
    def form_text_to_publish(self):
        status = ''
        if int(self.rating) <5:
            status+="It's bad restaurant"
        elif 5 <= int(self.rating) < 7:
            status += "It's mid-range restaurant"
        else:
            status += "It's great restaurant"
        text_to_publish ='Restaurant Review--------------------'+ '\n' + self.text + '\n' + status + '\n'
        return text_to_publish
