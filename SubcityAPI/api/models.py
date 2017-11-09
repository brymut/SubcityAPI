from django.db import models


# Create your models here.

class Shows(models.Model):
    """
     Show Model
    """
    shows_id = models.IntegerField(primary_key=True)
    shows_name = models.CharField(max_length=50)
    shows_text = models.TextField()
    shows_image_id = models.IntegerField()
    shows_cropped_image_id = models.IntegerField()
    shows_event = models.IntegerField(blank=True, null=True)
    shows_logname = models.CharField(unique=True, max_length=25)
    shows_sched_original_app_id = models.IntegerField(unique=True)
    show_on_break = models.IntegerField()
    objects = ShowsManager()

    class Meta:
        managed = False
        db_table = 'shows'


class ShowsManager(models.Manager):
    def search(self, search_terms):
        terms = [term.strip() for term in search_terms.split()]
        print(terms)
        q_objects = []

        for term in terms:
            q_objects.append(Q(shows_name__icontains=term))

        # Start with a bare QuerySet
        qs = self.get_queryset()

        # Use operator's or_ to string together all of your Q objects.
        return qs.filter(reduce(operator.and_, q_objects))
