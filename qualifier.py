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
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        self._words = {}
        self._count_words()

    def _count_words(self):
        words = self.content.split(" ")
        for word in words:
            if word in self._words:
                self._words[word] += 1
            else:
                self._words[word] = 1

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
        pass

    def __len__(self):
        return len(self.content)

    def __repr__(self):
        return (
            f'<Article title="{self.title}" '
            f"author='{self.author}' "
            f"publication_date='{self.publication_date.isoformat()}'>"
        )
