posts = [
    {
        'id': i,
        'title': 'Заголовок {}'.format(i),
        'description': 'Краткая информация'.format(i),
        'text': 'Подробная информация'.format(i)
    } for i in range(1, 9)
    ]

posts_dict = {val.get('id'): val for val in posts}