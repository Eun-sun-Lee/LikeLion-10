from django.db import models
from matplotlib.cbook import maxdict

class Blog(models.Model): # models.Model 상속 받아서 사용
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 객체를 처음 생성해줄때만 값 update

    def __str__(self):
        return self.title

