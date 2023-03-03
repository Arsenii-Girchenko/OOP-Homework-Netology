from pprint import pprint
import os
        
def read_files_from_folder(folder_name):
    file_description_dict = {}
    for filename in os.scandir(os.path.join(os.getcwd(), folder_name)):
        file_content_dict = {'strings amount': 0, 'text': ''}
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            lines_amount = len(lines)
            file_content_dict['strings amount'] = lines_amount
            file_content_dict['text'] += (''.join(lines))
        file_description_dict[filename] = file_content_dict
    return file_description_dict


def write_content_to_file(file_description_dict):
    length_dict = {}
    for filename, content in file_description_dict.items():
        length_dict[str(filename)] = content['strings amount']
        sorted(length_dict.items(), key=lambda x: x[0])
    result_string = ''
    for key, values in length_dict.items():
        for filename, content in file_description_dict.items():
            if content['strings amount'] == values:
                result_string += filename.name + '\n' + str(content['strings amount']) + '\n' + str(content['text']) + '\n'
    pprint(result_string)
    with open('result.txt', 'w') as result:
        result.writelines(result_string)
    return

write_content_to_file(read_files_from_folder('text_files'))