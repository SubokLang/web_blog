import datetime
import uuid
from src.common.database import Database

class Post():

    def __init__(self, blog_id, title, content, author,created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls,id):
        # print(id)
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

        '''
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   created_date=post_data['created_data'],
                   _id=post_data['_id'])
        '''

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]