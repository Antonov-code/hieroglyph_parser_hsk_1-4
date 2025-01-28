from bs4 import BeautifulSoup
import requests
import xlsxwriter

# BASE_URL = 'https://уроки-китайского.рф/spisok-slov-dlya-podgotovki-k-hsk-'

def query(url):
    r = requests.get(url)
    print(r.status_code)
    return r.content

def openFile (filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def main():
    i = 1
    allCharcter = []
    while i <= 4:
        level = []
        # q = query(BASE_URL + str(i) + '/')
        # html = BeautifulSoup(q, 'html.parser')
        content = openFile (f'hsk_{i}.html')
        html = BeautifulSoup(content, 'html.parser')
        for element in html.select(".has-fixed-layout > tbody > tr "):
            row = []
            c = 1
            for column in element.select("td"):
                number = BeautifulSoup(str(column), 'html.parser')
                row.append(number.find('td').text)
                c += 1
            level.append(row)
        i += 1
        allCharcter.append(level)
        
    l = 1
    for level in allCharcter:
        workbook = xlsxwriter.Workbook(f'result/hsk_{l}.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        column = 0
        for item in level :
            column = 0
            for i in item :
                worksheet.write(row, column, i)
                column += 1
            row += 1
        l += 1
        workbook.close()

if __name__ == "__main__":
    main()


# url = 'https://уроки-китайского.рф/spisok-slov-dlya-podgotovki-k-hsk'

# i = 1
# while i <= 4:
#     response = requests.get(f'{url}-{i}')

#     if response.status_code == 200:
#         html_content = response.text

#         with open(f'hsk_{i}.html', 'w', encoding='utf-8') as file:
#             file.write(html_content)
#         print('file saved successfully')
#     else:
#         print(f'Error :{response.status_code}')
