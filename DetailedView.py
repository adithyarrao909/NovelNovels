def book_detail_view(api_data):
    for item in api_data:
        volume_info = item['volumeInfo']
        PgCnt = volume_info['pageCount']
        title = volume_info['title']
        language = volume_info['language']
        authors = volume_info.get('authors', ['Unknown'])

        

        print("\033[1;36m╔══════════════════════╗\033[0m")
        print("\033[1;36m║\033[0m \033[1mTitle:\033[0m", title)
        print("\033[1;36m║\033[0m \033[1mPage Count:\033[0m", PgCnt)
        print("\033[1;36m║\033[0m \033[1mAuthors:\033[0m", ', '.join(authors))
        print("\033[1;36m║\033[0m \033[1mLanguage:\033[0m", language)
        print("\033[1;36m╚══════════════════════╝\033[0m")
        