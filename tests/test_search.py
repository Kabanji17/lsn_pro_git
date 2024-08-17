import pytest

from src.article import Article


@pytest.fixture
def list_articles():
    Article.articles = dict()  # зачищаем список статей
    Article.insert("title1", "content1")
    Article.insert("title2", "content2")
    Article.insert("title3", "content3")
    Article.insert("title4", "content4")
    return Article.insert("title5", "content5")


def test_search_3(list_articles):
    """Тестирование поиска статьи по ID"""
    searchable_article = Article.search(3)
    assert searchable_article.title == "title3"
    assert searchable_article.content == "content3"


def test_search_4(list_articles):
    """Тестирование поиска статьи по ID"""
    searchable_article = Article.search(4)
    assert searchable_article.title == "title4"
    assert searchable_article.content == "content4"
