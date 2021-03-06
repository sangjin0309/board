from datetime import datetime

from flask_mongoengine import Document
from mongoengine import StringField, DateTimeField, BooleanField


class Board(Document):
    name = StringField(required=True, description='게시판 이름')
    created_time = DateTimeField(default=datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'), description='게시판 생성일')
    deleted = BooleanField(default=False, description='삭제 여부')
    deleted_time = DateTimeField(null=True, default=None, description='게시판 삭제 시간')

    # 게시판 삭제
    def soft_delete(self):
        self.deleted = True
        self.deleted_time = datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')
        self.save()