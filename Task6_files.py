import os
import re

from Classes import Publication
from Task4_functions import capitalize_text


class FromTXT(Publication):
    def __init__(self, record_index, input_filename, file_path=os.path.dirname(__file__)):
        self.record_index = record_index
        self.input_filename = os.path.join(file_path, input_filename)
        self.file_path = file_path

    def form_text_to_publish(self):
        try:
            with open(self.input_filename, 'r') as file:
                data = file.readlines()
            data_str = ''.join(data)
            pattern = r'(News|Restaurant Review|Private advertisement)-+[-\n](.*?)(?=\n\n|\Z)'
            processed_data = re.findall(pattern, data_str, flags=re.DOTALL)
            result=''
            if len(processed_data)> self.record_index>=0:
                part_of_data = processed_data[:self.record_index]
            elif self.record_index<0 and (0-self.record_index)< len(processed_data):
                part_of_data = processed_data[self.record_index:]
            else:
                raise Exception('record_index is not valid')
            for i, part in enumerate(part_of_data):
                title, content = part
                result+="\n"+f"{title}------------\n"+content.strip() + "\n"
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
def create_publication_from_txt(record_index, input_filename, output_filename, file_path=os.path.dirname(__file__)):
    d = FromTXT(record_index, input_filename, file_path)
    d.publish(output_filename)