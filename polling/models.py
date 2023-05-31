from django.db import models

# Create your models here.

# auto_now_add for all the datetime field
class agentname(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.firstname}"


    class Meta:
        verbose_name_plural = 'agentnames'



class announced_lga_results(models.Model):
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.PositiveIntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.lga_name}"


    class Meta:
        verbose_name_plural = 'announced_lga_results'




class announced_pu_results(models.Model):
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.PositiveIntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.party_abbreviation}"


    class Meta:
        verbose_name_plural = 'announced_pu_results'




class announced_state_results(models.Model):
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.PositiveIntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.state_name}"


    class Meta:
        verbose_name_plural = 'announced_state_results'




class announced_ward_results(models.Model):
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.PositiveIntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ward_name}"


    class Meta:
        verbose_name_plural = 'announced_ward_results'




class lga(models.Model):
    lga_id = models.PositiveIntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.PositiveIntegerField()
    lga_description = models.TextField(max_length=1000)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.lga_name}"


    class Meta:
        verbose_name_plural = 'lgas'




class party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)


    def __str__(self):
        return f"{self.partyname}"


    class Meta:
        verbose_name_plural = 'parties'




class polling_unit(models.Model):
    polling_unit_id = models.PositiveIntegerField()
    ward_id = models.PositiveIntegerField()
    lga_id = models.PositiveIntegerField()
    uniquewardid = models.PositiveIntegerField(null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField(max_length=1000, null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.polling_unit_name}, {self.polling_unit_number}"


    class Meta:
        verbose_name_plural = 'polling_units'




class states(models.Model):
    state_id = models.PositiveIntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.state_name}"


    class Meta:
        verbose_name_plural = 'states'





class ward(models.Model):
    ward_id = models.PositiveIntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.PositiveIntegerField()
    ward_description = models.TextField(max_length=1000)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.ward_name}"

    class Meta:
        verbose_name_plural = 'wards'




