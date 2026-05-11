class Book:
    """
    Represents a single book object.
    """

    def __init__(self, title, author, status="Available"):
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        """
        Converts the object into dictionary format.
        """
        return {
            "title": self.title,
            "author": self.author,
            "status": self.status
        }

    def __str__(self):
        return f"{self.title} by {self.author} | {self.status}"