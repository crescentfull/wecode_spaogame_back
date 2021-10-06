from django.db       import models
from users.models    import User
from products.models import Product
from users.models    import TimeStampedModel

class Posting(TimeStampedModel):
    user_id         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    posting_id      = models.ForeignKey('postings.Product', on_delete=models.CASCADE)
    title           = models.CharField(max_length=100)
    content         = models.TextField()
    rating          = models.IntegerField()

    class Meta:
        db_table = 'postings'
        
class Comment(TimeStampedModel):
    user_id         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product_id      = models.ForeignKey('postings.Product', on_delete=models.CASCADE)
    postings_id     = models.ForeignKey('Posting', on_delete=models.CASCADE)
    contents        = models.TextField()
  
    class Meta:
        db_table = 'comments'  
