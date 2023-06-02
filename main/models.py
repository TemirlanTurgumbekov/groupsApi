from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    psevdonim = models.CharField(max_length=100, blank=True)

    def __str__(self):
        if self.psevdonim:
            return self.psevdonim
        return f'{self.name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Musician, related_name='songs', on_delete=models.CASCADE)
    feat = models.ForeignKey(Musician, on_delete=models.SET_NULL, null=True, related_name='feats', blank=True)
    poster = models.ImageField(upload_to='images/')
    year = models.DateField()

    def __str__(self):
        if self.feat:
            return f'{self.author} - {self.title} ft. {self.feat}'
        return f'{self.author} - {self.title}'


class Granny(models.Model):
    owner = models.OneToOneField(Musician, on_delete=models.CASCADE)
    year = models.DateField()
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.owner} - {self.year}'


    class Meta:
        verbose_name = 'Grammy'
        verbose_name_plural = 'Grammies'
