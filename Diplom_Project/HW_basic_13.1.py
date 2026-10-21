def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    while '<' in html:
        start = html.find('<')
        end = html.find('>')
        html = html[:start] + html[end + 1:]

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(html)

    print(html)

delete_html_tags('draft.html')

