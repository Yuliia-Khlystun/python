import json
import os
import re
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
        text_to_publish = '\n'+ 'News--------------------'+ '\n' + self.text + "\n" + self.city + '\n' + str(datetime.now().date()) + '\n'
        return text_to_publish
class PrivateAd(Publication):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = expiration_date
    def form_text_to_publish(self):
        target_date = datetime.strptime(self.expiration_date, "%Y-%m-%d").date()
        date_difference = target_date - datetime.now().date()
        text_to_publish = '\n'+ 'Private advertisement--------------------'+ '\n' +self.text + '\n' + str(date_difference.days) + ' days left' + '\n'
        return text_to_publish
class RestaurantReview(Publication):
    def __init__(self, text, rating):
        super().__init__(text)
        self.rating=rating
    def form_text_to_publish(self):
        status = ''
        if float(self.rating) <5:
            status+="It's bad restaurant"
        elif 5 <= float(self.rating) < 7:
            status += "It's mid-range restaurant"
        else:
            status += "It's great restaurant"
        text_to_publish ='\n'+'Restaurant Review--------------------'+ '\n' + self.text + '\n' + status + '\n'
        return text_to_publish
class FromTXT(Publication):
    def __init__(self, record_index, input_filename):
        self.record_index = record_index
        self.input_filename = input_filename

    def form_text_to_publish(self):
        try:
            with open(self.input_filename, 'r') as file:
                data = file.readlines()
            data_str = ''.join(data)
            pattern = r'(News|Restaurant Review|Private advertisement)-+[-\n](.*?)(?=\n\n|\Z)'
            processed_data = re.findall(pattern, data_str, flags=re.DOTALL)
            result=''
            if len(processed_data)> int(self.record_index)>=0:
                part_of_data = processed_data[:int(self.record_index)]
            elif int(self.record_index)<0 and (0-int(self.record_index))< len(processed_data):
                part_of_data = processed_data[int(self.record_index):]
            else:
                part_of_data = processed_data
            for i, part in enumerate(part_of_data):
                title, content = part
                result+="\n"+f"{title}------------\n"+content.strip() + "\n"
            from Task6.Task4_functions import capitalize_text
            capitalized_result=capitalize_text(result)
            return capitalized_result
        except FileNotFoundError:
            print(f"File {self.input_filename} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def publish(self, file_name):
        try:
            with open(file_name, 'a') as file:
                file.write(self.form_text_to_publish())
            os.remove(self.input_filename)
            print(f"Input file '{self.input_filename}' has been removed after processing.")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

class FromJSON(FromTXT):
    def __init__(self, record_index, input_filename):
        self.record_index = record_index
        self.input_filename = input_filename
    def form_text_to_publish(self):
        try:
            with open(self.input_filename, 'r') as file:
                data = json.load(file)
            if len(data)> int(self.record_index)>=0:
                part_of_data = data[:int(self.record_index)]
            elif int(self.record_index)<0 and (0-int(self.record_index))< len(data):
                part_of_data = data[int(self.record_index):]
            else:
                part_of_data = data
            text_to_pub=''
            for item in part_of_data:
                if item['type'] == 'News':
                    text_to_pub+=News(item['text'], item['city']).form_text_to_publish()
                elif item['type'] == 'PrivateAd':
                    text_to_pub+=PrivateAd(item['text'], item['expiration_date']).form_text_to_publish()
                elif item['type'] == 'RestaurantReview':
                    text_to_pub += RestaurantReview(item["text"], item['rating']).form_text_to_publish()
            return text_to_pub
        except FileNotFoundError:
            print(f"File {self.input_filename} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
