"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import re
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type
        self._value = None

    def __set__(self, instance, value: typing.Any):
        if not isinstance(value, self.field_type):
            raise TypeError(
                f"expected an instance of type '{self.field_type.__name__}' for attribute '{self.name}'"
                f", got '{type(value).__name__}' instead"
            )
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set_name__(self, owner, name):
        self.name = name


class Article:
    """The `Article` class you need to write for the qualifier."""

    article_counter = 0

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        self.id = self.get_article_id()
        self.last_edited = None

    @classmethod
    def get_article_id(cls):
        tmp_id = cls.article_counter
        cls.article_counter += 1
        return tmp_id

    def _count_words(self):
        count_words = {}
        words = re.findall(r"\w+", self.content)
        for word in words:
            if word.lower() in count_words:
                count_words[word.lower()] += 1
            else:
                count_words[word.lower()] = 1
        return count_words

    def short_introduction(self, n_characters: int):
        short_intro = self.content[:n_characters]
        newline_index = short_intro.rindex("\n") if "\n" in short_intro else 0
        space_index = short_intro.rindex(" ") if " " in short_intro else 0
        if newline_index > space_index:
            short_intro = short_intro[:newline_index]
        else:
            short_intro = short_intro[:space_index]
        return short_intro

    def most_common_words(self, n_words: int):
        words = self._count_words()
        most_common = {
            k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)[:n_words]
        }
        return most_common

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_content: str):
        self.last_edited = datetime.datetime.now()
        self._content = new_content

    def __len__(self):
        return len(self.content)

    def __lt__(self, other: "Article"):
        return self.publication_date < other.publication_date

    def __gt__(self, other: "Article"):
        return self.publication_date > other.publication_date

    def __eq__(self, other: "Article"):
        return self.publication_date == other.publication_date

    def __le__(self, other: "Article"):
        return self.publication_date <= other.publication_date

    def __ge__(self, other: "Article"):
        return self.publication_date >= other.publication_date

    def __ne__(self, other: "Article"):
        return self.publication_date != other.publication_date

    def __repr__(self):
        return (
            f'<Article title="{self.title}" '
            f"author='{self.author}' "
            f"publication_date='{self.publication_date.isoformat()}'>"
        )
