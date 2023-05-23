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

def is_vacances(date):
    # Définition des périodes de vacances scolaires en France pour les années 2019 à 2023
    vacances = [
        ('2019-02-16', '2019-03-04'),  # Vacances d'hiver 2019
        ('2019-04-06', '2019-04-22'),  # Vacances de printemps 2019
        ('2019-07-06', '2019-09-02'),  # Vacances d'été 2019
        ('2019-10-19', '2019-11-04'),  # Vacances de Toussaint 2019
        ('2019-12-21', '2020-01-06'),  # Vacances de Noël 2019
        ('2020-02-15', '2020-03-02'),  # Vacances d'hiver 2020
        ('2020-04-04', '2020-04-20'),  # Vacances de printemps 2020
        ('2020-07-04', '2020-08-31'),  # Vacances d'été 2020
        ('2020-10-17', '2020-11-02'),  # Vacances de Toussaint 2020
        ('2020-12-19', '2021-01-04'),  # Vacances de Noël 2020
        ('2021-02-06', '2021-02-22'),  # Vacances d'hiver 2021
        ('2021-04-10', '2021-04-26'),  # Vacances de printemps 2021
        ('2021-07-10', '2021-08-30'),  # Vacances d'été 2021
        ('2021-10-23', '2021-11-08'),  # Vacances de Toussaint 2021
        ('2021-12-18', '2022-01-03'),  # Vacances de Noël 2021
        ('2022-02-19', '2022-03-07'),  # Vacances d'hiver 2022
        ('2022-04-09', '2022-04-25'),  # Vacances de printemps 2022
        ('2022-07-09', '2022-09-05'),  # Vacances d'été 2022
        ('2022-10-22', '2022-11-07'),  # Vacances de Toussaint 2022
        ('2022-12-17', '2023-01-02'),  # Vacances de Noël 2022
        ('2023-02-18', '2023-03-06'),  # Vacances d'hiver 2023
        ('2023-04-08', '2023-04-24'),  # Vacances de printemps 2023
        ('2023-07-08', '2023-09-04'),  # Vacances d'été 2023
        ('2023-10-21', '2023-11-06'),  # Vacances de Toussaint 2023
        ('2023-12-23', '2024-01-08') # Vacances de Noël 2023
    ]
    
    # Vérification si la date est incluse dans une période de vacances
    for debut, fin in vacances:
        if debut <= date <= fin:
            return True
    return False