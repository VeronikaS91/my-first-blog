from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model): # bude definovat, jak se bude příspěvek v blogu chovat
	author = models.ForeignKey(
		'auth.User',
		on_delete = models.CASCADE) # když smažu uživatele, tak se smažou všechny jeho příspěvky kaskádovitě
	title = models.CharField(max_length=200) #Charfield je text (maximální délka našeho textového příspěvku bude 200 znaků)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now) #default = výchozí hodnota bude dnešní čas
	publish_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self): 
		self.publish_date = timezone.now()
		self.save()

	def __str__(self): # tímto říkáme, jak se bude příspěvek převádět na řetězec
		return self.title

