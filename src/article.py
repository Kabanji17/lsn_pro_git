class Article:
    """Класс для хранения статьи"""

    article_id: int
    title: str
    content: str

    articles = dict()  # атрибут на уровне класса для хранения всех статей

    def __init__(self, title: str, content: str):
        """Конструктор для статьи"""
        self.article_id = self.get_new_id()
        self.title = title
        self.content = content

    def get_new_id(self) -> int:
        """Метод для получения ID следующей статьи"""
        if len(self.articles) > 0:
            return max(self.articles.keys()) + 1
        return 1

    @classmethod
    def insert(cls, title: str, content: str):
        """Метод для создания и добавления статьи"""
        new_article = cls(title, content)
        cls.articles[new_article.article_id] = new_article
        return new_article

    @classmethod
    def search(cls, article_id):
        """Метод для поиска статьи по ID"""
        # return cls("title3", "content3")
        return cls.articles[article_id]


if __name__ == "__main__":
    art_1 = Article.insert("title1", "content1")
    print(art_1.article_id)

    art_2 = Article.insert("title2", "content2")
    print(art_2.article_id)
