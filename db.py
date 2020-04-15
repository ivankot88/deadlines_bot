import peewee
import datetime
database = peewee.SqliteDatabase("database.db")

class Deadlines(peewee.Model):
    id = peewee.IntegerField()
    name = peewee.CharField()
    date = peewee.DateField(default=datetime.date.today)
    class Meta:
        database = database
