class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Invalid title length")

        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        results = []
        for a in Article.all:
            if a.author == self:
                results.append(a)
        return results

    def magazines(self):
        mags = []
        arts = self.articles()
        for art in arts:
            m = art.magazine
            if m not in mags:
                mags.append(m)
        return mags

    def add_article(self, magazine, title):
        a = Article(self, magazine, title)
        return a

    def topic_areas(self):
        arts = self.articles()
        if len(arts) == 0:
            return None

        areas = []
        mags = self.magazines()
        for m in mags:
            c = m.category
            if c not in areas:
                areas.append(c)
        return areas


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Invalid name")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Invalid category")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 2 and len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and value != "":
            self._category = value

    def articles(self):
        result = []
        for a in Article.all:
            if a.magazine == self:
                result.append(a)
        return result

    def contributors(self):
        authors = []
        arts = self.articles()
        for a in arts:
            if a.author not in authors:
                authors.append(a.author)
        return authors

    def article_titles(self):
        arts = self.articles()
        if len(arts) == 0:
            return None
        titles = []
        for a in arts:
            titles.append(a.title)
        return titles

    def contributing_authors(self):
        counts = {}
        arts = self.articles()
        for a in arts:
            auth = a.author
            if auth in counts:
                counts[auth] += 1
            else:
                counts[auth] = 1

        finals = []
        for auth, num in counts.items():
            if num > 2:
                finals.append(auth)

        if len(finals) == 0:
            return None
        return finals
