# ADOFAI – Guide de configuration (Setup)

## 📦 Prérequis

- **Archipelago** : version minimale recommandée : `6.3.0`
- **ADOFAI** : version stable compatible avec le monde
- **Client** : [Client Mod BepInEx](https://github.com/ClaudeChibout/ADOFAI_AP-Mod/releases/tag/v2.0.0-beta)
- Connexion internet stable

---

## 📥 Installation du Mod

1. Glisser le contenu de l'archive du client dans le dossier d'installation de ADOFAI

---

## ⚙️ Configuration du slot

La configuration se fait depuis la **page des options joueur** :  
👉 [Options joueur ADOFAI](../player-options)

### Options disponibles

| Option | Description |
|--------|-------------|
| **percentage_goal_completion** | Pourcentage de niveaux à compléter pour la victoire |
| **completion_goal** | Mode de définition de l’objectif final (`allX`, `goalLevels`) |
| **goal_levels** | Liste des niveaux requis si `completion_goal = goalLevels` |
| **main_worlds_tuto** | Inclut les tutoriels des mondes principaux |
| **xtra_worlds** | Ajoute les mondes xtra |
| **xtra_worlds_tuto** | Ajoute les tutoriels des mondes xtra |
| **b_world** | Ajoute le monde B |
| **b_world_tuto** | Ajoute le tutoriel du monde B |
| **crown_worlds** | Ajoute les mondes “Crown” |
| **crown_worlds_tuto** | Ajoute les tutoriels des mondes “Crown” |
| **star_worlds** | Ajoute les mondes “Star” |
| **star_worlds_tuto** | Ajoute les tutoriels des mondes “Star” |
| **neon_cosmos_worlds** | Ajoute les mondes “Neon Cosmos” standards |
| **neon_cosmos_worlds_tuto** | Ajoute les tutoriels “Neon Cosmos” standards |
| **neon_cosmos_worlds_ex** | Ajoute les mondes “Neon Cosmos EX” |
| **neon_cosmos_worlds_ex_tuto** | Ajoute les tutoriels “Neon Cosmos EX” |
| **april_fools_worlds** | Ajoute les mondes “April Fools” |
| **cosmic_radio_worlds** | Ajoute les mondes “Cosmic Radio” (CE, CI) |
| **cosmic_radio_worlds_tuto** | Ajoute les tutoriels des mondes “Cosmic Radio” |
| **cosmic_radio_worlds_ex** | Ajoute le monde “Cosmic Radio EX” (CE-TX, très difficile) |
| **death_link** | Active le DeathLink entre joueurs |

---

## 🎮 Lancer une partie locale

1. Mettre son YAML dans `Archipelago\Players`
2. Dans **Archipelago**, choisir **Generate**.
3. Dans **Archipelago**, choisir **Host** et selectionner l'archive nouvellement crée dans `Archipelago\output`.

---

## 🌍 Jouer en Multiworld

1. Héberger un serveur Archipelago ou rejoindre celui d’un autre joueur.
2. Récupérer le fichier de configuration `.yaml` correspondant à votre slot.
3. Lancer le jeu avec le client configuré (ADOFAI modifié).
4. Connectez-vous au serveur avec :
- **Adresse**
- **Port**
- **Nom de slot**

---

## 🏁 Objectif et progression

- **Début** : vous avez accès à un petit nombre de niveaux initiaux.
- **Progression** : chaque niveau terminé donne un **objet**.
- **Victoire** : Remplissez vos conditions de victoire spécifié dans votre YAML pour gagner.

