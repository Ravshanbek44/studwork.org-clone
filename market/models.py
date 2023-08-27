from django.db import models
from project.models import WorkType
from user.models import Subject, Account


class Market(models.Model):
    COURSE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Subject, on_delete=models.CASCADE)
    univer_name = models.CharField(max_length=120)
    course = models.IntegerField(choices=COURSE, default=0)
    description = models.TextField()
    content = models.TextField()
    list_lit = models.TextField()
    is_top = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class MarketFileDemo(models.Model):
    file = models.FileField(upload_to='market_files/')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='file_demo')


class MarketFileDone(models.Model):
    file = models.FileField(upload_to='market_files/')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='file_done')
