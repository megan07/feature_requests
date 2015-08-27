from django.db import models

# Client Model
class Client(models.Model):
    client_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' %(self.client_name)


# Feature Request Model
class FeatureRequest(models.Model):

    POLICIES = 'policies'
    BILLING = 'billing'
    CLAIMS = 'claims'
    REPORTS = 'reports'

    PRODUCT_CHOICES = (
        (POLICIES, 'Policies'),
        (BILLING, 'Billing'),
        (CLAIMS, 'Claims'),
        (REPORTS, 'Reports')
    )

    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    client =  models.ForeignKey(Client, verbose_name="Client", null=True, default=None, blank=True)
    priority = models.IntegerField(verbose_name="Priority", default=0)
    target_date = models.DateField(max_length=10, verbose_name="Target Date")
    tix_url = models.CharField(max_length=200, verbose_name="Ticket URL")

    product_area = models.CharField(max_length=10,
                                    verbose_name="Product Area",
                                    choices=PRODUCT_CHOICES,
                                    default=POLICIES)

    body_html = models.TextField(blank=True)


    class Meta:
        ordering = ('-target_date', '-priority')


    def __unicode__(self):
        return u'%s' %(self.title)
