import datetime
import holidays

def is_ferie(date):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    annee = date_obj.year

    jours_feries = holidays.France(years=annee)
    if date_obj in jours_feries:
        return True
    else:
        return False
