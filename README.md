# GestionCabinetMedical

**Projet Django — Gestion des rendez-vous d'un cabinet médical**
**Etudiante :** Chadha Boughanmi
**Classe :** 3A19  
**Année universitaire :** 2026–2027  
**Framework :** Django 5.2

## 1. Présentation

Ce projet consiste à développer une application web de gestion des rendez-vous d'un cabinet médical à l'aide du framework Django.

Il permet de gérer les médecins, les patients, les spécialités médicales et les rendez-vous à travers l'interface d'administration Django.

## 2. Technologies utilisées

- Python 3.12
- Django 5.2 LTS
- SQLite
- HTML (interface d'administration Django)
- Git et GitHub
- Visual Studio Code

## 3. Structure du projet

- `GestionCabinetMedical/` : configuration principale du projet Django.
- `Medecin/` : gestion des médecins et des spécialités.
- `Patient/` : gestion des patients.
- `RendezVous/` : gestion des rendez-vous médicaux.
- `Cabinet/` : application créée lors de la configuration initiale.
- `manage.py` : exécution des commandes Django.
- `requirements.txt` : dépendances Python.

## 4. Fonctionnalités réalisées

### Gestion des médecins
- Création et gestion des comptes médecins.
- Validation du matricule d'ordre et du téléphone.
- Association des médecins à plusieurs spécialités.

### Gestion des patients
- Création et gestion des comptes patients.
- Validation du CIN et du numéro de téléphone.
- Vérification de la date de naissance.
- Consultation de l'historique des rendez-vous.

### Gestion des rendez-vous
- Création de rendez-vous entre médecins et patients.
- Gestion des statuts : En attente, Confirmé et Annulé.
- Validation des dates de rendez-vous.
- Prévention des rendez-vous ayant le même médecin et la même date/heure.
- Ajout facultatif d'ordonnances au format PDF.
- Filtres par statut, médecin et période.
- Actions de confirmation et d'annulation.
- Affichage de la durée des rendez-vous confirmés du jour.

## 5. Installation et exécution

Cloner le dépôt :

```bash
git clone https://github.com/chadha23/GestionCabinetMedical.git
cd GestionCabinetMedical
```

Créer l'environnement virtuel avec Python 3.12 :

```cmd
py -3.12 -m venv env
```

Activer l'environnement sous Windows CMD :

```cmd
env\Scripts\activate.bat
```

Installer les dépendances :

```cmd
python -m pip install -r requirements.txt
```

Créer les tables de la base de données :

```cmd
python manage.py migrate
```

Créer un compte administrateur :

```cmd
python manage.py createsuperuser
```

Lancer le serveur :

```cmd
python manage.py runserver
```

Accéder à l'administration Django :

`http://127.0.0.1:8000/admin/`

**Remarque :** La base de données locale et l'environnement virtuel ne sont pas inclus dans le dépôt GitHub. Ils sont recréés lors de l'installation. Les données de démonstration doivent être ajoutées séparément.

## 6. Conclusion

Ce travail met en application les notions de modélisation avec l'ORM Django, les relations entre modèles, la validation des données, les migrations et la personnalisation du Back-Office Django.